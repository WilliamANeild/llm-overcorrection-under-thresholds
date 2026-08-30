"use client";

import { useState, useEffect, useCallback } from "react";

interface Pair {
  pair_id: string;
  task_prompt: string;
  output_a: string;
  output_b: string;
  domain: string;
}

interface Choice {
  pair_id: string;
  choice: "A" | "B";
}

const ALLOWED_RATERS = ["liam"];

export default function ComparePage() {
  const [raterId, setRaterId] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [loginError, setLoginError] = useState("");
  const [pairs, setPairs] = useState<Pair[]>([]);
  const [choices, setChoices] = useState<Record<string, "A" | "B">>({});
  const [skipped, setSkipped] = useState<Set<string>>(new Set());
  const [currentIdx, setCurrentIdx] = useState(0);
  const [loading, setLoading] = useState(true);
  const [highlight, setHighlight] = useState<"A" | "B" | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  // Load pairs
  useEffect(() => {
    fetch("/t1_vs_t5_pairs.json")
      .then((r) => r.json())
      .then((data: Pair[]) => {
        setPairs(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  // Restore from localStorage
  useEffect(() => {
    if (typeof window === "undefined") return;
    const saved = localStorage.getItem("t1v5_session");
    if (saved) {
      try {
        const { id, choices: c, skipped: s, idx } = JSON.parse(saved);
        if (id && ALLOWED_RATERS.includes(id)) {
          setRaterId(id);
          setLoggedIn(true);
          setChoices(c || {});
          setSkipped(new Set(s || []));
          setCurrentIdx(idx || 0);
        }
      } catch (_) { /* ignore corrupt localStorage */ }
    }
  }, []);

  // Save to localStorage on change
  useEffect(() => {
    if (!loggedIn) return;
    localStorage.setItem(
      "t1v5_session",
      JSON.stringify({
        id: raterId,
        choices,
        skipped: Array.from(skipped),
        idx: currentIdx,
      })
    );
  }, [loggedIn, raterId, choices, skipped, currentIdx]);

  // Clamp currentIdx when pairs change (e.g. data shrinks after redeployment)
  useEffect(() => {
    if (pairs.length > 0 && currentIdx >= pairs.length) {
      setCurrentIdx(0);
    }
  }, [pairs, currentIdx]);

  // Keyboard shortcuts
  useEffect(() => {
    if (!loggedIn || submitted || pairs.length === 0) return;
    const handler = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
      if (e.key === "ArrowLeft") handleChoice("A");
      else if (e.key === "ArrowRight") handleChoice("B");
      else if (e.key === "s" || e.key === "S") handleSkip();
      else if (e.key === "ArrowUp") goTo(Math.max(0, currentIdx - 1));
      else if (e.key === "ArrowDown") goTo(Math.min(pairs.length - 1, currentIdx + 1));
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  });

  const handleLogin = () => {
    const id = raterId.trim().toLowerCase();
    if (!ALLOWED_RATERS.includes(id)) {
      setLoginError("Access restricted. Only authorized raters can use this page.");
      return;
    }
    setRaterId(id);
    setLoggedIn(true);
    setLoginError("");
  };

  const handleChoice = useCallback(
    (choice: "A" | "B") => {
      if (pairs.length === 0) return;
      const pair = pairs[currentIdx];
      setChoices((prev) => ({ ...prev, [pair.pair_id]: choice }));
      setHighlight(choice);
      setTimeout(() => {
        setHighlight(null);
        if (currentIdx < pairs.length - 1) {
          setCurrentIdx((i) => i + 1);
        }
      }, 250);
    },
    [currentIdx, pairs]
  );

  const handleSkip = () => {
    if (pairs.length === 0) return;
    const pair = pairs[currentIdx];
    setSkipped((prev) => new Set(prev).add(pair.pair_id));
    if (currentIdx < pairs.length - 1) setCurrentIdx((i) => i + 1);
  };

  const goTo = (idx: number) => {
    setCurrentIdx(idx);
    setHighlight(null);
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    const choiceArray: Choice[] = Object.entries(choices).map(([pair_id, choice]) => ({
      pair_id,
      choice,
    }));
    try {
      const res = await fetch("/api/submit-comparison", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          rater_id: raterId,
          choices: choiceArray,
          skipped: Array.from(skipped),
        }),
      });
      if (res.ok) setSubmitted(true);
    } catch (_) { /* ignore network error */ }
    setSubmitting(false);
  };

  const handleReset = () => {
    if (confirm("Reset all progress? This cannot be undone.")) {
      localStorage.removeItem("t1v5_session");
      setChoices({});
      setSkipped(new Set());
      setCurrentIdx(0);
    }
  };

  const totalDone = Object.keys(choices).length;
  const pct = pairs.length > 0 ? Math.round((totalDone / pairs.length) * 100) : 0;

  // ---- Login Screen ----
  if (!loggedIn) {
    return (
      <div style={styles.container}>
        <div style={styles.loginCard}>
          <h1 style={styles.title}>T1 vs T5 Comparison</h1>
          <p style={styles.subtitle}>Human validation of revision quality</p>
          <input
            type="text"
            placeholder="Enter your rater ID"
            value={raterId}
            onChange={(e) => setRaterId(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleLogin()}
            style={styles.input}
            autoFocus
          />
          {loginError && <p style={styles.error}>{loginError}</p>}
          <button onClick={handleLogin} style={styles.loginBtn}>
            Start
          </button>
        </div>
      </div>
    );
  }

  // ---- Loading ----
  if (loading || pairs.length === 0) {
    return (
      <div style={styles.container}>
        <p style={{ color: "#999" }}>Loading pairs...</p>
      </div>
    );
  }

  // ---- Submitted ----
  if (submitted) {
    return (
      <div style={styles.container}>
        <div style={styles.loginCard}>
          <h1 style={styles.title}>Done!</h1>
          <p style={styles.subtitle}>
            {totalDone} choices submitted. {skipped.size > 0 && `(${skipped.size} skipped)`}
          </p>
          <p style={{ color: "#888", fontSize: 14 }}>Results saved to server. You can close this tab.</p>
        </div>
      </div>
    );
  }

  // ---- Main UI ----
  const pair = pairs[currentIdx];
  if (!pair) {
    return (
      <div style={styles.container}>
        <p style={{ color: "#999" }}>No pairs available. Try resetting.</p>
      </div>
    );
  }
  const currentChoice = choices[pair.pair_id] || null;
  const isSkipped = skipped.has(pair.pair_id);

  return (
    <div style={styles.page}>
      {/* Header */}
      <div style={styles.header}>
        <div style={styles.headerLeft}>
          <h2 style={{ margin: 0, fontSize: 16, color: "#fff" }}>T1 vs T5 Comparison</h2>
          <span style={styles.badge}>{pair.domain}</span>
          <span style={{ color: "#666", fontSize: 13 }}>
            {currentIdx + 1} / {pairs.length}
          </span>
        </div>
        <div style={styles.headerRight}>
          <div style={styles.progressBarOuter}>
            <div style={{ ...styles.progressBarInner, width: `${pct}%` }} />
          </div>
          <span style={{ color: "#aaa", fontSize: 12 }}>{totalDone} done</span>
          <button onClick={handleReset} style={styles.resetBtn}>Reset</button>
          {totalDone === pairs.length && (
            <button onClick={handleSubmit} disabled={submitting} style={styles.submitBtn}>
              {submitting ? "Submitting..." : "Submit All"}
            </button>
          )}
        </div>
      </div>

      {/* Instructions (collapsible) */}
      <details style={styles.instructions}>
        <summary style={{ cursor: "pointer", color: "#aaa", fontSize: 13 }}>Instructions</summary>
        <p style={{ margin: "8px 0 0", color: "#888", fontSize: 13, lineHeight: 1.5 }}>
          For each pair, read the task prompt and both outputs. Choose which output better fulfills
          the task. Judge on task fulfillment, completeness, correctness, and clarity. Do NOT
          consider length as a quality signal. Use arrow keys (left = A, right = B) for speed. Press S to skip.
        </p>
      </details>

      {/* Task Prompt */}
      <div style={styles.taskPrompt}>
        <span style={{ color: "#666", fontSize: 11, textTransform: "uppercase", letterSpacing: 1 }}>
          Task Prompt
        </span>
        <p style={{ margin: "4px 0 0", color: "#ddd", fontSize: 14, lineHeight: 1.5 }}>
          {pair.task_prompt}
        </p>
      </div>

      {/* Side-by-side outputs */}
      <div style={styles.outputGrid}>
        <div
          style={{
            ...styles.outputPanel,
            borderColor: highlight === "A" ? "#3b82f6" : currentChoice === "A" ? "#3b82f655" : "#333",
            background: highlight === "A" ? "#1a2a40" : currentChoice === "A" ? "#111827" : "#0d0d0d",
          }}
        >
          <div style={styles.outputHeader}>
            <span style={{ fontWeight: 700, color: "#3b82f6" }}>Output A</span>
            {currentChoice === "A" && <span style={styles.chosenBadge}>Chosen</span>}
          </div>
          <div style={styles.outputText}>{pair.output_a}</div>
        </div>
        <div
          style={{
            ...styles.outputPanel,
            borderColor: highlight === "B" ? "#f59e0b" : currentChoice === "B" ? "#f59e0b55" : "#333",
            background: highlight === "B" ? "#2a2210" : currentChoice === "B" ? "#1c1a0f" : "#0d0d0d",
          }}
        >
          <div style={styles.outputHeader}>
            <span style={{ fontWeight: 700, color: "#f59e0b" }}>Output B</span>
            {currentChoice === "B" && <span style={{ ...styles.chosenBadge, background: "#f59e0b33", color: "#f59e0b" }}>Chosen</span>}
          </div>
          <div style={styles.outputText}>{pair.output_b}</div>
        </div>
      </div>

      {/* Action buttons */}
      <div style={styles.actions}>
        <button
          onClick={() => goTo(Math.max(0, currentIdx - 1))}
          disabled={currentIdx === 0}
          style={styles.navBtn}
        >
          Prev
        </button>
        <button onClick={() => handleChoice("A")} style={styles.choiceBtn}>
          <span style={{ fontSize: 11, color: "#666" }}>&#8592;</span> A is better
        </button>
        <button onClick={handleSkip} style={styles.skipBtn}>
          Skip{isSkipped ? "ped" : ""}
        </button>
        <button onClick={() => handleChoice("B")} style={{ ...styles.choiceBtn, background: "#f59e0b22", borderColor: "#f59e0b55", color: "#f59e0b" }}>
          B is better <span style={{ fontSize: 11, color: "#666" }}>&#8594;</span>
        </button>
        <button
          onClick={() => goTo(Math.min(pairs.length - 1, currentIdx + 1))}
          disabled={currentIdx === pairs.length - 1}
          style={styles.navBtn}
        >
          Next
        </button>
      </div>

      {/* Pair navigator dots */}
      <div style={styles.dots}>
        {pairs.map((p, i) => (
          <div
            key={p.pair_id}
            onClick={() => goTo(i)}
            style={{
              width: 8,
              height: 8,
              borderRadius: 4,
              cursor: "pointer",
              background: choices[p.pair_id]
                ? "#3b82f6"
                : skipped.has(p.pair_id)
                ? "#666"
                : i === currentIdx
                ? "#fff"
                : "#333",
              transition: "background 0.15s",
            }}
          />
        ))}
      </div>
    </div>
  );
}

// ---- Styles ----

const styles: Record<string, React.CSSProperties> = {
  container: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    background: "#0a0a0a",
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
  },
  page: {
    minHeight: "100vh",
    background: "#0a0a0a",
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    padding: "16px 24px",
    display: "flex",
    flexDirection: "column",
    gap: 12,
  },
  loginCard: {
    background: "#111",
    border: "1px solid #222",
    borderRadius: 12,
    padding: "40px 48px",
    textAlign: "center",
    maxWidth: 400,
  },
  title: { color: "#fff", fontSize: 24, margin: "0 0 8px" },
  subtitle: { color: "#888", fontSize: 14, margin: "0 0 24px" },
  input: {
    width: "100%",
    padding: "12px 16px",
    background: "#1a1a1a",
    border: "1px solid #333",
    borderRadius: 8,
    color: "#fff",
    fontSize: 15,
    outline: "none",
    marginBottom: 12,
  },
  error: { color: "#ef4444", fontSize: 13, margin: "0 0 12px" },
  loginBtn: {
    width: "100%",
    padding: "12px",
    background: "#3b82f6",
    border: "none",
    borderRadius: 8,
    color: "#fff",
    fontSize: 15,
    fontWeight: 600,
    cursor: "pointer",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    paddingBottom: 8,
    borderBottom: "1px solid #222",
  },
  headerLeft: { display: "flex", alignItems: "center", gap: 12 },
  headerRight: { display: "flex", alignItems: "center", gap: 12 },
  badge: {
    padding: "2px 8px",
    background: "#1a1a2e",
    border: "1px solid #333",
    borderRadius: 4,
    fontSize: 11,
    color: "#aaa",
    textTransform: "uppercase" as const,
  },
  progressBarOuter: {
    width: 120,
    height: 6,
    background: "#222",
    borderRadius: 3,
    overflow: "hidden",
  },
  progressBarInner: {
    height: "100%",
    background: "#3b82f6",
    transition: "width 0.3s",
    borderRadius: 3,
  },
  submitBtn: {
    padding: "6px 16px",
    background: "#22c55e",
    border: "none",
    borderRadius: 6,
    color: "#fff",
    fontSize: 13,
    fontWeight: 600,
    cursor: "pointer",
  },
  resetBtn: {
    padding: "4px 10px",
    background: "transparent",
    border: "1px solid #333",
    borderRadius: 4,
    color: "#666",
    fontSize: 11,
    cursor: "pointer",
  },
  instructions: {
    background: "#111",
    border: "1px solid #222",
    borderRadius: 8,
    padding: "8px 12px",
  },
  taskPrompt: {
    background: "#111",
    border: "1px solid #222",
    borderRadius: 8,
    padding: "12px 16px",
  },
  outputGrid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: 12,
    flex: 1,
    minHeight: 0,
  },
  outputPanel: {
    border: "2px solid #333",
    borderRadius: 10,
    padding: 16,
    display: "flex",
    flexDirection: "column",
    overflow: "hidden",
    transition: "border-color 0.2s, background 0.2s",
  },
  outputHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 8,
    paddingBottom: 8,
    borderBottom: "1px solid #222",
  },
  outputText: {
    color: "#ccc",
    fontSize: 13,
    lineHeight: 1.6,
    whiteSpace: "pre-wrap" as const,
    overflow: "auto",
    flex: 1,
    maxHeight: "45vh",
  },
  chosenBadge: {
    padding: "2px 8px",
    background: "#3b82f633",
    borderRadius: 4,
    fontSize: 11,
    color: "#3b82f6",
    fontWeight: 600,
  },
  actions: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    gap: 12,
    padding: "8px 0",
  },
  choiceBtn: {
    padding: "10px 24px",
    background: "#3b82f622",
    border: "1px solid #3b82f655",
    borderRadius: 8,
    color: "#3b82f6",
    fontSize: 14,
    fontWeight: 600,
    cursor: "pointer",
  },
  skipBtn: {
    padding: "8px 16px",
    background: "transparent",
    border: "1px solid #333",
    borderRadius: 8,
    color: "#666",
    fontSize: 12,
    cursor: "pointer",
  },
  navBtn: {
    padding: "8px 12px",
    background: "transparent",
    border: "1px solid #222",
    borderRadius: 6,
    color: "#666",
    fontSize: 12,
    cursor: "pointer",
  },
  dots: {
    display: "flex",
    justifyContent: "center",
    gap: 4,
    flexWrap: "wrap" as const,
    padding: "4px 0",
  },
};
