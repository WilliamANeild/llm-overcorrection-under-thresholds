#!/usr/bin/env python3
"""A paragraph-at-a-time writing desk for the paper.

Stdlib only, no installs.

    python3 paper/writer/serve.py
    open http://127.0.0.1:8787

Drafts autosave to paper/writer/drafts/:
    state.json        machine state (text + checkboxes)
    introduction.md   readable mirror, one beat per heading

Nothing here writes to paper/sections/. Export is explicit and lands in drafts/.
"""

import json
import http.server
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
DRAFTS.mkdir(exist_ok=True)
STATE = DRAFTS / "state.json"
OUTLINE = ROOT / "outline.json"
PORT = 8787


# Existing prose, shown collapsed in the UI as a reference. Read live from the
# section files so it never drifts. Paragraphs map to beats in order.
CURRENT_SOURCES = {"introduction": ROOT.parent / "sections" / "introduction_v2.tex"}


def current_paragraphs(path):
    if not path.exists():
        return []
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.lstrip().startswith("%")]
    body = "\n".join(lines)
    body = body.split("}", 1)[1] if body.lstrip().startswith("\\section{") else body
    paras = []
    for chunk in body.split("\n\n"):
        text = " ".join(chunk.split())
        if len(text.split()) > 25:
            paras.append(text)
    return paras


def read_outline():
    outline = json.loads(OUTLINE.read_text(encoding="utf-8"))
    for section in outline["sections"]:
        paras = current_paragraphs(CURRENT_SOURCES.get(section["id"], Path("/nonexistent")))
        for i, beat in enumerate(section["beats"]):
            if i < len(paras):
                beat["current"] = paras[i]
    return outline


def read_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def write_mirrors(state):
    """Write a human-readable Markdown mirror per section."""
    outline = read_outline()
    for section in outline["sections"]:
        lines = ["# " + section["title"], ""]
        total = 0
        for beat in section["beats"]:
            key = section["id"] + "." + beat["id"]
            text = (state.get(key, {}) or {}).get("text", "").strip()
            total += len(text.split())
            lines.append("## Beat {}. {}".format(beat["id"][1:], beat["title"]))
            lines.append("")
            lines.append(text if text else "_(empty)_")
            lines.append("")
        lines.insert(1, "")
        lines.insert(1, "_{} words drafted._".format(total))
        (DRAFTS / (section["id"] + ".md")).write_text(
            "\n".join(lines), encoding="utf-8"
        )


def export_tex(section_id):
    outline = read_outline()
    state = read_state()
    section = next(s for s in outline["sections"] if s["id"] == section_id)
    chunks = ["\\section{" + section["title"] + "}", ""]
    for beat in section["beats"]:
        key = section_id + "." + beat["id"]
        text = (state.get(key, {}) or {}).get("text", "").strip()
        if text:
            chunks.append("% Beat {}. {}".format(beat["id"][1:], beat["title"]))
            chunks.append(text)
            chunks.append("")
    path = DRAFTS / (section_id + "_draft.tex")
    path.write_text("\n".join(chunks), encoding="utf-8")
    return path


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # quiet

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, (ROOT / "app.html").read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/outline":
            self._send(200, json.dumps(read_outline()))
        elif self.path == "/state":
            self._send(200, json.dumps(read_state()))
        else:
            self._send(404, json.dumps({"error": "not found"}))

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            self._send(400, json.dumps({"error": "bad json"}))
            return

        if self.path == "/save":
            state = read_state()
            state[payload["key"]] = {
                "text": payload.get("text", ""),
                "checked": payload.get("checked", []),
            }
            STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")
            write_mirrors(state)
            self._send(200, json.dumps({"ok": True}))
        elif self.path == "/export":
            path = export_tex(payload.get("section", "introduction"))
            self._send(200, json.dumps({"ok": True, "path": str(path)}))
        else:
            self._send(404, json.dumps({"error": "not found"}))


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Server(("127.0.0.1", PORT), Handler) as httpd:
        print("Writing desk at http://127.0.0.1:{}".format(PORT))
        print("Drafts saving to {}".format(DRAFTS))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped")
