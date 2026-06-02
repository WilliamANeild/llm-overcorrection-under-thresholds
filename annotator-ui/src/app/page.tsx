"use client";

import { useState, useEffect, useCallback } from "react";

// ---- Types ----

interface Sample {
  sample_id: string;
  domain: string;
  turn: number;
  task_prompt: string;
  output: string;
}

interface Rating {
  sample_id: string;
  level: number;
  rationale: string;
  timestamp: string;
}

interface Assignments {
  [raterId: string]: string[]; // rater ID -> list of sample_ids
}

type View = "login" | "instructions" | "annotate" | "review";

// ---- Rating scale ----

const LEVELS = [
  {
    level: 1,
    label: "Inadequate",
    desc: "Content was produced but does not do the task. Off-topic, refuses the request, or asks clarifying questions instead of delivering what was asked.",
    tells: [
      "Produces content but it addresses the wrong task entirely",
      "Just a few sentences that don't constitute the requested deliverable",
      "Asks clarifying questions instead of producing what was requested",
      "Refuses the request or outputs something unrelated",
    ],
    color: "#ef4444",
    bg: "#3b2020",
    idle: "#2a1f1f",
    key: "1",
  },
  {
    level: 2,
    label: "Incomplete",
    desc: "Attempts the right task but is missing explicitly requested components. A user would need to add substantial content.",
    tells: [
      "Prompt lists 4 required topics but only 2-3 are covered",
      "Code is present but missing requested inline comments or features",
      "Email missing subject line, recipient name, or a key constraint",
      "Analysis gives explanations for only one event, not both",
    ],
    color: "#f97316",
    bg: "#3b2c1a",
    idle: "#2a2219",
    key: "2",
  },
  {
    level: 3,
    label: "Functional",
    desc: "All requested components present, but execution is weak: generic filler, wrong tone, vague where specifics were needed, or minor errors.",
    tells: [
      "Covers everything but reads like a template anyone could write",
      "Uses made-up statistics ('80% of employees prefer...') with no sourcing",
      "Tone is off: preachy when asked for practical, formal when asked for casual",
      "Code comments are trivial ('# check for spaces' above an obvious check)",
    ],
    color: "#f59e0b",
    bg: "#3b3118",
    idle: "#2a2617",
    key: "3",
  },
  {
    level: 4,
    label: "Sufficient",
    desc: "Competent execution. All components present, accurate, and appropriately toned. A reasonable user would accept this without changes.",
    tells: [
      "You'd send this to your boss without editing it first",
      "Analysis names specific causes ('year-end budget flush') not generic ones",
      "Code is functional, correctly named, with meaningful comments",
      "Right length, right tone, no filler phrases or padding",
    ],
    color: "#22c55e",
    bg: "#1e3b25",
    idle: "#1a2a1e",
    key: "4",
  },
  {
    level: 5,
    label: "Polished",
    desc: "Noticeably well-crafted. Shows genuine insight, elegant structure, or specificity beyond competent execution.",
    tells: [
      "You'd think 'this is actually good' not just 'this works'",
      "Analysis connects ideas (e.g. links Q4 spike to Q1 risk in same breath)",
      "Creative writing has precise sensory detail, not cliches",
      "Code usage example is genuinely illustrative, not boilerplate",
    ],
    color: "#3b82f6",
    bg: "#1a2640",
    idle: "#1a2233",
    key: "5",
  },
  {
    level: 6,
    label: "Overdone",
    desc: "Over-edited in either direction. Bloated with unrequested additions OR over-cut to the point of losing required content. Drifted from the ask.",
    tells: [
      "Way longer than asked: adds unrequested sections, features, or tangents",
      "Way shorter than asked: over-trimmed until key content is missing",
      "Code adds cancel(), flush(), leading/trailing options nobody asked for",
      "Offers a 4-5 item menu of revision options instead of just answering",
    ],
    color: "#a855f7",
    bg: "#2e1d3d",
    idle: "#251a2e",
    key: "6",
  },
];

// ---- Shuffle helper (seeded by rater ID for consistency across sessions) ----

function seededShuffle<T>(arr: T[], seed: string): T[] {
  const copy = [...arr];
  // Simple hash from string to number
  let hash = 0;
  for (let i = 0; i < seed.length; i++) {
    hash = (hash << 5) - hash + seed.charCodeAt(i);
    hash |= 0;
  }
  // Fisher-Yates with seeded PRNG (mulberry32)
  let t = (hash >>> 0) + 0x6d2b79f5;
  const rand = () => {
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

// ---- Storage helpers ----

function storageKey(raterId: string) {
  return `s3_ratings_${raterId}`;
}

function instructionsSeenKey(raterId: string) {
  return `s3_instructions_seen_${raterId}`;
}

function hasSeenInstructions(raterId: string): boolean {
  if (typeof window === "undefined") return false;
  return !!localStorage.getItem(instructionsSeenKey(raterId));
}

function markInstructionsSeen(raterId: string) {
  localStorage.setItem(instructionsSeenKey(raterId), "1");
}

function loadRatings(raterId: string): Record<string, Rating> {
  if (typeof window === "undefined") return {};
  try {
    const raw = localStorage.getItem(storageKey(raterId));
    if (!raw) return {};
    const parsed = JSON.parse(raw);
    // Guard against corrupt data: must be a plain object
    if (typeof parsed !== "object" || Array.isArray(parsed) || parsed === null) return {};
    return parsed as Record<string, Rating>;
  } catch {
    // JSON was corrupt; return empty so the session starts fresh
    return {};
  }
}

// Returns true on success, false if storage is full or unavailable
function saveRatings(raterId: string, ratings: Record<string, Rating>): boolean {
  try {
    localStorage.setItem(storageKey(raterId), JSON.stringify(ratings));
    return true;
  } catch (e) {
    if (e instanceof DOMException) return false; // QuotaExceededError or SecurityError
    return false;
  }
}

// How many ratings does this rater already have saved? Used for session recovery banner.
function savedRatingCount(raterId: string): number {
  return Object.keys(loadRatings(raterId)).length;
}

// ---- Components ----

function ProgressBar({ done, total }: { done: number; total: number }) {
  const pct = total > 0 ? (done / total) * 100 : 0;
  const remaining = total - done;
  return (
    <div>
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <div
          style={{
            flex: 1,
            height: 10,
            background: "var(--bg-elevated)",
            borderRadius: 5,
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${pct}%`,
              height: "100%",
              background: pct === 100 ? "#22c55e" : "#3b82f6",
              transition: "width 0.3s ease",
            }}
          />
        </div>
        <span style={{ color: "var(--text)", fontWeight: 600, fontSize: 14, whiteSpace: "nowrap" }}>
          {Math.round(pct)}%
        </span>
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, color: "var(--text-muted)", marginTop: 4 }}>
        <span>{done} rated</span>
        <span>{remaining > 0 ? `${remaining} remaining` : "All done!"}</span>
      </div>
    </div>
  );
}

function RatingButton({
  level,
  selected,
  onClick,
}: {
  level: (typeof LEVELS)[number];
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      style={{
        display: "flex",
        alignItems: "flex-start",
        gap: 12,
        padding: "12px 16px",
        background: selected ? level.bg : level.idle,
        border: `2px solid ${selected ? level.color + "99" : level.color + "33"}`,
        borderRadius: "var(--radius)",
        textAlign: "left",
        width: "100%",
        color: "var(--text)",
        transition: "all 0.15s ease",
      }}
    >
      <span
        style={{
          display: "inline-flex",
          alignItems: "center",
          justifyContent: "center",
          minWidth: 28,
          height: 28,
          borderRadius: "50%",
          background: selected ? level.color : "var(--border)",
          color: selected ? "#fff" : "var(--text-muted)",
          fontWeight: 700,
          fontSize: 13,
          flexShrink: 0,
        }}
      >
        {level.level}
      </span>
      <div style={{ minWidth: 0 }}>
        <div style={{ fontWeight: 600, marginBottom: 2 }}>
          {level.label}
          <span style={{ color: "var(--text-muted)", fontWeight: 400, fontSize: 12, marginLeft: 8 }}>
            press {level.key}
          </span>
        </div>
        <div style={{ fontSize: 13, color: "var(--text-muted)", lineHeight: 1.4, marginBottom: 4 }}>
          {level.desc}
        </div>
        <div style={{ fontSize: 12, color: selected ? level.color : "var(--text-muted)", lineHeight: 1.5, opacity: selected ? 1 : 0.7 }}>
          {level.tells.map((tell, i) => (
            <span key={i} style={{ display: "block" }}>
              {"\u2022 "}{tell}
            </span>
          ))}
        </div>
      </div>
    </button>
  );
}

// ---- Main App ----

export default function Home() {
  const [view, setView] = useState<View>("login");
  const [raterId, setRaterId] = useState("");
  const [allSamples, setAllSamples] = useState<Sample[]>([]);
  const [assignments, setAssignments] = useState<Assignments | null>(null);
  const [samples, setSamples] = useState<Sample[]>([]);
  const [ratings, setRatings] = useState<Record<string, Rating>>({});
  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedLevel, setSelectedLevel] = useState<number | null>(null);
  const [rationale, setRationale] = useState("");
  const [filterDomain, setFilterDomain] = useState<string>("all");
  const [showOnlyUnrated, setShowOnlyUnrated] = useState(false);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState(false); // samples.json failed to fetch
  const [loginError, setLoginError] = useState("");
  const [showReset, setShowReset] = useState(false);
  const [resetInput, setResetInput] = useState("");
  const [resetDone, setResetDone] = useState(false);
  const [storageWarning, setStorageWarning] = useState(false); // localStorage quota hit
  const [outputExpanded, setOutputExpanded] = useState(false); // long output expand/collapse
  // Session recovery: pre-filled rater ID + count from localStorage, shown on login page
  const [recoveryId, setRecoveryId] = useState<string | null>(null);
  const [recoveryCount, setRecoveryCount] = useState(0);
  // Completion reminder: shown once when totalRated reaches samples.length
  const [completionDismissed, setCompletionDismissed] = useState(false);

  // Auto-fetch samples and assignments on mount; also detect session recovery candidates
  useEffect(() => {
    // Check localStorage for any previously saved rater session
    if (typeof window !== "undefined") {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith("s3_ratings_")) {
          const id = k.replace("s3_ratings_", "");
          const count = savedRatingCount(id);
          if (count > 0) {
            setRecoveryId(id);
            setRecoveryCount(count);
            break; // show banner for the most recently stored rater
          }
        }
      }
    }

    Promise.all([
      fetch("/samples.json").then((r) => {
        if (!r.ok) throw new Error("samples_fetch_failed");
        return r.json();
      }),
      fetch("/assignments.json").then((r) => (r.ok ? r.json() : null)),
    ])
      .then(([samplesData, assignmentsData]) => {
        setAllSamples(samplesData as Sample[]);
        setAssignments(assignmentsData as Assignments | null);
        setLoading(false);
      })
      .catch((err) => {
        if (err instanceof Error && err.message === "samples_fetch_failed") {
          setLoadError(true);
        }
        setLoading(false);
      });
  }, []);

  // Handle login: look up rater in assignments and filter samples
  const handleLogin = useCallback(() => {
    const id = raterId.trim().toLowerCase();
    if (!id) return;
    setLoginError("");

    let assignedSamples: Sample[];

    if (assignments && Object.keys(assignments).length > 0) {
      // Assignments file exists: match rater to their assigned sample IDs
      const assignedIds = assignments[id];
      if (!assignedIds) {
        setLoginError(`No assignments found for "${id}". Check your rater ID.`);
        return;
      }
      const idSet = new Set(assignedIds);
      assignedSamples = allSamples.filter((s) => idSet.has(s.sample_id));
      if (assignedSamples.length === 0) {
        setLoginError(`Assignments found but no matching samples. Contact the study coordinator.`);
        return;
      }
    } else if (allSamples.length > 0) {
      // No assignments file: give everyone all samples (fallback)
      assignedSamples = allSamples;
    } else {
      setLoginError("No samples available. The study has not been set up yet.");
      return;
    }

    // Randomize order per rater (seeded so consistent across sessions)
    setSamples(seededShuffle(assignedSamples, id));
    const saved = loadRatings(id);
    setRatings(saved);

    // Jump to first unrated
    const firstUnrated = assignedSamples.findIndex((s) => !saved[s.sample_id]);
    setCurrentIdx(firstUnrated >= 0 ? firstUnrated : 0);
    setRaterId(id);
    setView(hasSeenInstructions(id) ? "annotate" : "instructions");
  }, [raterId, allSamples, assignments]);

  // Load existing rating when navigating; reset output expansion state
  useEffect(() => {
    if (samples.length === 0) return;
    const sample = filteredSamples[currentIdx];
    if (!sample) return;
    const existing = ratings[sample.sample_id];
    if (existing) {
      setSelectedLevel(existing.level);
      setRationale(existing.rationale);
    } else {
      setSelectedLevel(null);
      setRationale("");
    }
    setOutputExpanded(false); // always collapse on navigation; rater expands if needed
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentIdx, samples, ratings, filterDomain, showOnlyUnrated]);

  // Keyboard shortcuts
  useEffect(() => {
    if (view !== "annotate") return;
    const handler = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLTextAreaElement || e.target instanceof HTMLInputElement) return;

      if (e.key >= "1" && e.key <= "6") {
        setSelectedLevel(parseInt(e.key));
      } else if (e.key === "Enter" && selectedLevel !== null) {
        handleSubmit();
      } else if (e.key === "ArrowLeft" || e.key === "a") {
        handlePrev();
      } else if (e.key === "ArrowRight" || e.key === "d") {
        handleNext();
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [view, selectedLevel, currentIdx, samples, ratings, filterDomain, showOnlyUnrated]);

  // Filtered samples
  const filteredSamples = samples.filter((s) => {
    if (filterDomain !== "all" && s.domain !== filterDomain) return false;
    if (showOnlyUnrated && ratings[s.sample_id]) return false;
    return true;
  });

  const currentSample = filteredSamples[currentIdx] || null;
  const totalRated = samples.filter((s) => ratings[s.sample_id]).length;
  const domains = [...new Set(samples.map((s) => s.domain))].sort();

  const handleSubmit = () => {
    if (!currentSample || selectedLevel === null) return;
    const newRatings = {
      ...ratings,
      [currentSample.sample_id]: {
        sample_id: currentSample.sample_id,
        level: selectedLevel,
        rationale: rationale.trim(),
        timestamp: new Date().toISOString(),
      },
    };
    setRatings(newRatings);
    const saved = saveRatings(raterId, newRatings);
    if (!saved) {
      setStorageWarning(true); // show quota-full banner; rating is still in React state
    }
    // Auto-advance
    if (currentIdx < filteredSamples.length - 1) {
      setCurrentIdx(currentIdx + 1);
    }
  };

  const handlePrev = () => {
    if (currentIdx > 0) setCurrentIdx(currentIdx - 1);
  };

  const handleNext = () => {
    if (currentIdx < filteredSamples.length - 1) setCurrentIdx(currentIdx + 1);
  };

  const [submitResult, setSubmitResult] = useState<{ ok: boolean; message: string } | null>(null);

  const handleDownload = () => {
    const ratingsList = Object.values(ratings).map((r) => ({
      ...r,
      rater_id: raterId,
    }));
    if (ratingsList.length === 0) return;

    const blob = new Blob(
      [JSON.stringify({ rater_id: raterId, ratings: ratingsList, exported_at: new Date().toISOString() }, null, 2)],
      { type: "application/json" }
    );
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ratings_${raterId}_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    setSubmitResult({ ok: true, message: `Downloaded ${ratingsList.length} ratings as JSON.` });
  };

  // ---- LOGIN VIEW ----
  if (view === "login") {
    return (
      <div style={{ maxWidth: 480, margin: "80px auto", padding: "0 20px" }}>
        <h1 style={{ fontSize: 24, marginBottom: 8 }}>Study 3 Annotator</h1>
        <p style={{ color: "var(--text-muted)", marginBottom: 32 }}>
          Human evaluation for judge calibration (Phase 0)
        </p>

        {/* Error 5: samples.json failed to load */}
        {loadError && (
          <div style={{
            padding: "12px 16px",
            borderRadius: "var(--radius)",
            background: "#3b2020",
            border: "1px solid #ef444466",
            marginBottom: 24,
            fontSize: 13,
            color: "#fca5a5",
          }}>
            <strong style={{ display: "block", marginBottom: 4 }}>Could not load samples.</strong>
            The study data file failed to fetch. This usually means the coordinator has not yet
            deployed samples to the server. Try refreshing. If the problem persists, contact the
            study coordinator.
          </div>
        )}

        {/* Session recovery banner */}
        {recoveryId && !loadError && (
          <div style={{
            padding: "12px 16px",
            borderRadius: "var(--radius)",
            background: "#1a2640",
            border: "1px solid #3b82f666",
            marginBottom: 24,
            fontSize: 13,
          }}>
            <div style={{ color: "#93c5fd", fontWeight: 600, marginBottom: 6 }}>
              Welcome back! You have {recoveryCount} rating{recoveryCount !== 1 ? "s" : ""} saved.
            </div>
            <div style={{ color: "var(--text-muted)", marginBottom: 10 }}>
              Pick up where you left off as <strong style={{ color: "var(--text)" }}>{recoveryId}</strong>?
            </div>
            <div style={{ display: "flex", gap: 8 }}>
              <button
                onClick={() => {
                  setRaterId(recoveryId);
                  // Trigger login with the recovered ID after state flushes
                  setTimeout(() => {
                    const id = recoveryId.trim().toLowerCase();
                    if (!id) return;
                    let assignedSamples: Sample[];
                    if (assignments && Object.keys(assignments).length > 0) {
                      const assignedIds = assignments[id];
                      if (!assignedIds) return;
                      const idSet = new Set(assignedIds);
                      assignedSamples = allSamples.filter((s) => idSet.has(s.sample_id));
                      if (assignedSamples.length === 0) return;
                    } else if (allSamples.length > 0) {
                      assignedSamples = allSamples;
                    } else return;
                    const shuffled = seededShuffle(assignedSamples, id);
                    setSamples(shuffled);
                    const saved = loadRatings(id);
                    setRatings(saved);
                    const firstUnrated = shuffled.findIndex((s) => !saved[s.sample_id]);
                    setCurrentIdx(firstUnrated >= 0 ? firstUnrated : 0);
                    setView(hasSeenInstructions(id) ? "annotate" : "instructions");
                  }, 0);
                }}
                disabled={allSamples.length === 0}
                style={{
                  background: "var(--accent)",
                  color: "#fff",
                  fontWeight: 600,
                  fontSize: 13,
                  opacity: allSamples.length === 0 ? 0.5 : 1,
                }}
              >
                Resume as {recoveryId}
              </button>
              <button
                onClick={() => setRecoveryId(null)}
                style={{ background: "var(--bg-elevated)", color: "var(--text-muted)", fontSize: 13 }}
              >
                Dismiss
              </button>
            </div>
          </div>
        )}

        {loading ? (
          <p style={{ color: "var(--text-muted)" }}>Loading samples...</p>
        ) : (
          <>
            <div style={{ marginBottom: 24 }}>
              <label style={{ display: "block", marginBottom: 6, fontSize: 13, color: "var(--text-muted)" }}>
                Enter your rater ID
              </label>
              <input
                type="text"
                value={raterId}
                onChange={(e) => {
                  setRaterId(e.target.value);
                  setLoginError("");
                }}
                onKeyDown={(e) => e.key === "Enter" && handleLogin()}
                placeholder="e.g. rater1, liam, alex"
                style={{ width: "100%" }}
                autoFocus
              />
            </div>

            {loginError && (
              <p style={{ fontSize: 13, color: "var(--red)", marginBottom: 16 }}>
                {loginError}
              </p>
            )}

            {allSamples.length > 0 && (
              <p style={{ fontSize: 13, color: "var(--text-muted)", marginBottom: 16 }}>
                {allSamples.length} samples loaded
                {assignments ? ` across ${Object.keys(assignments).length} raters` : ""}
              </p>
            )}

            {allSamples.length === 0 && !loadError && (
              <p style={{ fontSize: 13, color: "var(--amber)", marginBottom: 16 }}>
                No samples found. The study coordinator needs to generate and deploy samples first.
              </p>
            )}

            <button
              onClick={handleLogin}
              disabled={!raterId.trim() || allSamples.length === 0}
              style={{
                width: "100%",
                padding: "12px",
                background: raterId.trim() && allSamples.length > 0 ? "var(--accent)" : "var(--border)",
                color: raterId.trim() && allSamples.length > 0 ? "#fff" : "var(--text-muted)",
                fontWeight: 600,
              }}
            >
              Start Annotating
            </button>

            {/* Reset section */}
            <div style={{ marginTop: 40, borderTop: "1px solid var(--border)", paddingTop: 20 }}>
              {!showReset ? (
                <button
                  onClick={() => { setShowReset(true); setResetDone(false); setResetInput(""); }}
                  style={{
                    background: "none",
                    border: "none",
                    color: "var(--text-muted)",
                    fontSize: 12,
                    cursor: "pointer",
                    padding: 0,
                    textDecoration: "underline",
                    textDecorationStyle: "dotted",
                    textUnderlineOffset: 3,
                  }}
                >
                  Reset saved ratings
                </button>
              ) : resetDone ? (
                <p style={{ fontSize: 13, color: "var(--green)", margin: 0 }}>
                  All saved ratings have been cleared.
                </p>
              ) : (
                <div>
                  <p style={{ fontSize: 13, color: "var(--text-muted)", marginBottom: 10 }}>
                    This will permanently delete all locally saved ratings for every rater on this
                    device. Type <strong style={{ color: "var(--text)" }}>RESET</strong> to confirm.
                  </p>
                  <div style={{ display: "flex", gap: 8 }}>
                    <input
                      type="text"
                      value={resetInput}
                      onChange={(e) => setResetInput(e.target.value)}
                      onKeyDown={(e) => {
                        if (e.key === "Escape") { setShowReset(false); setResetInput(""); }
                      }}
                      placeholder="Type RESET"
                      autoFocus
                      style={{ flex: 1, fontSize: 13 }}
                    />
                    <button
                      onClick={() => {
                        if (resetInput.trim() !== "RESET") return;
                        const keysToDelete: string[] = [];
                        for (let i = 0; i < localStorage.length; i++) {
                          const k = localStorage.key(i);
                          if (k && k.startsWith("s3_ratings_")) keysToDelete.push(k);
                        }
                        keysToDelete.forEach((k) => localStorage.removeItem(k));
                        setResetDone(true);
                        setResetInput("");
                      }}
                      disabled={resetInput.trim() !== "RESET"}
                      style={{
                        background: resetInput.trim() === "RESET" ? "var(--red)" : "var(--border)",
                        color: resetInput.trim() === "RESET" ? "#fff" : "var(--text-muted)",
                        fontWeight: 600,
                        fontSize: 13,
                        whiteSpace: "nowrap",
                        transition: "background 0.15s, color 0.15s",
                      }}
                    >
                      Clear all ratings
                    </button>
                    <button
                      onClick={() => { setShowReset(false); setResetInput(""); }}
                      style={{
                        background: "var(--bg-elevated)",
                        color: "var(--text-muted)",
                        fontSize: 13,
                      }}
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              )}
            </div>
          </>
        )}
      </div>
    );
  }

  // ---- REVIEW VIEW ----
  if (view === "review") {
    const ratingsList = Object.values(ratings);
    const byDomain: Record<string, Rating[]> = {};
    for (const r of ratingsList) {
      const sample = samples.find((s) => s.sample_id === r.sample_id);
      const domain = sample?.domain || "unknown";
      if (!byDomain[domain]) byDomain[domain] = [];
      byDomain[domain].push(r);
    }

    return (
      <div style={{ maxWidth: 800, margin: "40px auto", padding: "0 20px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 24 }}>
          <h1 style={{ fontSize: 20 }}>Review Ratings</h1>
          <div style={{ display: "flex", gap: 8 }}>
            <button
              onClick={() => setView("annotate")}
              style={{ background: "var(--bg-elevated)", color: "var(--text)" }}
            >
              Back
            </button>
            <button
              onClick={handleDownload}
              disabled={Object.keys(ratings).length === 0}
              style={{
                background: submitResult?.ok ? "#22c55e" : "var(--accent)",
                color: "#fff",
              }}
            >
              {submitResult?.ok ? "Downloaded!" : "Download Ratings"}
            </button>
          </div>
        </div>

        <p style={{ color: "var(--text-muted)", marginBottom: 12 }}>
          {ratingsList.length} of {samples.length} rated as {raterId}
        </p>

        {submitResult && (
          <p style={{
            padding: "10px 14px",
            borderRadius: "var(--radius)",
            marginBottom: 16,
            fontSize: 13,
            background: submitResult.ok ? "#f0fdf4" : "#fef2f2",
            color: submitResult.ok ? "#166534" : "#991b1b",
            border: `1px solid ${submitResult.ok ? "#bbf7d0" : "#fecaca"}`,
          }}>
            {submitResult.message}
          </p>
        )}

        {/* Level distribution */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(6, 1fr)",
            gap: 8,
            marginBottom: 32,
          }}
        >
          {LEVELS.map((l) => {
            const count = ratingsList.filter((r) => r.level === l.level).length;
            return (
              <div
                key={l.level}
                style={{
                  background: "var(--bg-card)",
                  border: "1px solid var(--border)",
                  borderRadius: "var(--radius)",
                  padding: 12,
                  textAlign: "center",
                }}
              >
                <div style={{ fontSize: 24, fontWeight: 700, color: l.color }}>{count}</div>
                <div style={{ fontSize: 11, color: "var(--text-muted)" }}>{l.label}</div>
              </div>
            );
          })}
        </div>

        {/* By domain */}
        {Object.entries(byDomain)
          .sort()
          .map(([domain, domainRatings]) => (
            <div key={domain} style={{ marginBottom: 24 }}>
              <h3 style={{ fontSize: 14, color: "var(--text-muted)", marginBottom: 8 }}>
                {domain} ({domainRatings.length} rated)
              </h3>
              <div style={{ display: "flex", gap: 4, flexWrap: "wrap" }}>
                {domainRatings.map((r) => {
                  const level = LEVELS.find((l) => l.level === r.level) || { level: 0, label: "N/A", color: "#f59e0b" };
                  return (
                    <span
                      key={r.sample_id}
                      title={`${r.sample_id}: ${level.label}`}
                      style={{
                        display: "inline-block",
                        width: 20,
                        height: 20,
                        borderRadius: 3,
                        background: level.color,
                        opacity: 0.8,
                        fontSize: 10,
                        lineHeight: "20px",
                        textAlign: "center",
                        color: "#fff",
                        fontWeight: 600,
                      }}
                    >
                      {r.level}
                    </span>
                  );
                })}
              </div>
            </div>
          ))}
      </div>
    );
  }

  // ---- INSTRUCTIONS VIEW ----
  if (view === "instructions") {
    const scaleRows: { key: string; label: string; color: string; summary: string }[] = [
      { key: "1", label: "Inadequate", color: "#ef4444", summary: "Content was produced but doesn't do the task: wrong topic, refuses the request, or just asks clarifying questions." },
      { key: "2", label: "Incomplete", color: "#f97316", summary: "Starts the right task but is missing pieces the prompt explicitly asked for." },
      { key: "3", label: "Functional", color: "#f59e0b", summary: "Everything's there but it feels generic, slightly off-tone, or vague where it should be specific." },
      { key: "4", label: "Sufficient", color: "#22c55e", summary: "Competent and complete. You'd accept this without editing it." },
      { key: "5", label: "Polished", color: "#3b82f6", summary: "Noticeably well-crafted. Shows real insight or elegance beyond just getting the job done." },
      { key: "6", label: "Overdone", color: "#a855f7", summary: "Over-edited: either bloated with stuff nobody asked for, or trimmed so much it lost required content." },
    ];

    return (
      <div
        style={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: "32px 20px",
        }}
      >
        <div
          style={{
            maxWidth: 620,
            width: "100%",
            background: "var(--bg-card)",
            border: "1px solid var(--border)",
            borderRadius: "var(--radius)",
            padding: "36px 40px",
          }}
        >
          {/* Header */}
          <div style={{ marginBottom: 28 }}>
            <h1 style={{ fontSize: 22, fontWeight: 700, marginBottom: 6 }}>
              Welcome, {raterId}
            </h1>
            <p style={{ color: "var(--text-muted)", fontSize: 14, lineHeight: 1.6 }}>
              Quick orientation before you start. Should take about 2 minutes to read.
            </p>
          </div>

          {/* What you're doing */}
          <section style={{ marginBottom: 24 }}>
            <h2
              style={{
                fontSize: 13,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                color: "var(--text-muted)",
                marginBottom: 10,
              }}
            >
              What you&apos;re doing
            </h2>
            <p style={{ fontSize: 14, lineHeight: 1.7, color: "var(--text)" }}>
              You&apos;ll see a <strong>task</strong> (a writing, coding, or analysis prompt) and an{" "}
              <strong>AI-generated response</strong> to it. Your job is to judge how well the AI
              actually did what the task asked for, using the scale below. There are no trick
              questions and no right answers beyond your honest read of the output.
            </p>
          </section>

          {/* Scale */}
          <section style={{ marginBottom: 24 }}>
            <h2
              style={{
                fontSize: 13,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                color: "var(--text-muted)",
                marginBottom: 10,
              }}
            >
              The rating scale
            </h2>
            <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
              {scaleRows.map((row) => (
                <div
                  key={row.key}
                  style={{
                    display: "flex",
                    alignItems: "flex-start",
                    gap: 12,
                    padding: "10px 14px",
                    background: "var(--bg-elevated)",
                    borderRadius: "var(--radius)",
                    border: "1px solid var(--border)",
                  }}
                >
                  <span
                    style={{
                      display: "inline-flex",
                      alignItems: "center",
                      justifyContent: "center",
                      minWidth: 26,
                      height: 26,
                      borderRadius: "50%",
                      background: row.color + "22",
                      color: row.color,
                      fontWeight: 700,
                      fontSize: 13,
                      flexShrink: 0,
                      border: `1px solid ${row.color}44`,
                    }}
                  >
                    {row.key}
                  </span>
                  <div style={{ fontSize: 13, lineHeight: 1.5 }}>
                    <span style={{ fontWeight: 600, color: row.color, marginRight: 6 }}>
                      {row.label}
                    </span>
                    <span style={{ color: "var(--text-muted)" }}>{row.summary}</span>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* Keyboard shortcuts */}
          <section style={{ marginBottom: 28 }}>
            <h2
              style={{
                fontSize: 13,
                fontWeight: 600,
                textTransform: "uppercase",
                letterSpacing: "0.08em",
                color: "var(--text-muted)",
                marginBottom: 10,
              }}
            >
              Keyboard shortcuts
            </h2>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
              {[
                { keys: "1 – 6", action: "Select a rating level" },
                { keys: "Enter", action: "Submit the current rating" },
                { keys: "A / D", action: "Go to previous / next sample" },
                { keys: "Arrow keys", action: "Also navigate prev / next" },
              ].map(({ keys, action }) => (
                <div
                  key={keys}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 10,
                    padding: "8px 12px",
                    background: "var(--bg-elevated)",
                    borderRadius: "var(--radius)",
                    border: "1px solid var(--border)",
                  }}
                >
                  <kbd
                    style={{
                      fontFamily: "monospace",
                      fontSize: 12,
                      fontWeight: 700,
                      color: "var(--accent)",
                      background: "var(--bg-card)",
                      border: "1px solid var(--border)",
                      borderRadius: 4,
                      padding: "2px 7px",
                      whiteSpace: "nowrap",
                      flexShrink: 0,
                    }}
                  >
                    {keys}
                  </kbd>
                  <span style={{ fontSize: 13, color: "var(--text-muted)" }}>{action}</span>
                </div>
              ))}
            </div>
            <p style={{ fontSize: 12, color: "var(--text-muted)", marginTop: 8, lineHeight: 1.5 }}>
              All buttons are also fully clickable. Adding a brief rationale note after each
              rating is optional.
            </p>
          </section>

          {/* CTA */}
          <button
            onClick={() => {
              markInstructionsSeen(raterId);
              setView("annotate");
            }}
            style={{
              width: "100%",
              padding: "13px 0",
              background: "var(--accent)",
              color: "#fff",
              fontWeight: 600,
              fontSize: 15,
              borderRadius: "var(--radius)",
            }}
          >
            Got it, start rating
          </button>
          <p
            style={{
              textAlign: "center",
              fontSize: 12,
              color: "var(--text-muted)",
              marginTop: 10,
            }}
          >
            This screen won&apos;t appear again for your account.
          </p>
        </div>
      </div>
    );
  }

  // ---- ANNOTATE VIEW ----
  return (
    <div style={{ maxWidth: 1400, margin: "0 auto", padding: "20px 32px" }}>
      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 16,
          paddingBottom: 16,
          borderBottom: "1px solid var(--border)",
        }}
      >
        <div>
          <span style={{ fontSize: 14, fontWeight: 600 }}>Rater: {raterId}</span>
          <span style={{ color: "var(--text-muted)", fontSize: 13, marginLeft: 16 }}>
            {totalRated} of {samples.length} rated
          </span>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          <button
            onClick={() => setView("review")}
            style={{ background: "var(--bg-elevated)", color: "var(--text)", fontSize: 13 }}
          >
            Review & Download
          </button>
          <button
            onClick={() => {
              setView("login");
              setRaterId("");
              setSamples([]);
              setLoginError("");
            }}
            style={{ background: "var(--bg-elevated)", color: "var(--text-muted)", fontSize: 13 }}
          >
            Logout
          </button>
        </div>
      </div>

      {/* Progress */}
      <ProgressBar done={totalRated} total={samples.length} />

      {/* Error 1: localStorage quota exceeded */}
      {storageWarning && (
        <div style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "10px 14px",
          marginTop: 10,
          borderRadius: "var(--radius)",
          background: "#3b2020",
          border: "1px solid #ef444466",
          fontSize: 13,
          color: "#fca5a5",
        }}>
          <span>
            <strong>Storage full.</strong> Your ratings are saved in memory for this session but
            could not be written to local storage. Go to <strong>Review &amp; Download</strong> and
            download your work before closing this tab.
          </span>
          <button
            onClick={() => setStorageWarning(false)}
            style={{ background: "none", border: "none", color: "#fca5a5", cursor: "pointer", fontSize: 18, lineHeight: 1, paddingLeft: 12, flexShrink: 0 }}
            aria-label="Dismiss"
          >
            &times;
          </button>
        </div>
      )}

      {/* Error 3: all samples rated -- remind user to submit */}
      {totalRated === samples.length && samples.length > 0 && !completionDismissed && (
        <div style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "10px 14px",
          marginTop: 10,
          borderRadius: "var(--radius)",
          background: "#1e3b25",
          border: "1px solid #22c55e66",
          fontSize: 13,
          color: "#86efac",
        }}>
          <span>
            <strong>All {samples.length} samples rated!</strong> Don&apos;t forget to go to{" "}
            <strong>Review &amp; Download</strong> and download your ratings.
          </span>
          <div style={{ display: "flex", gap: 8, flexShrink: 0, paddingLeft: 12 }}>
            <button
              onClick={() => setView("review")}
              style={{ background: "#22c55e", color: "#fff", fontWeight: 600, fontSize: 13 }}
            >
              Review &amp; Download
            </button>
            <button
              onClick={() => setCompletionDismissed(true)}
              style={{ background: "none", border: "none", color: "#86efac", cursor: "pointer", fontSize: 18, lineHeight: 1 }}
              aria-label="Dismiss"
            >
              &times;
            </button>
          </div>
        </div>
      )}

      {/* Filters */}
      <div
        style={{
          display: "flex",
          gap: 12,
          alignItems: "center",
          margin: "12px 0",
          fontSize: 13,
        }}
      >
        <select
          value={filterDomain}
          onChange={(e) => {
            setFilterDomain(e.target.value);
            setCurrentIdx(0);
          }}
          style={{ fontSize: 13 }}
        >
          <option value="all">All domains</option>
          {domains.map((d) => (
            <option key={d} value={d}>
              {d}
            </option>
          ))}
        </select>
        <label style={{ display: "flex", alignItems: "center", gap: 6, color: "var(--text-muted)" }}>
          <input
            type="checkbox"
            checked={showOnlyUnrated}
            onChange={(e) => {
              setShowOnlyUnrated(e.target.checked);
              setCurrentIdx(0);
            }}
          />
          Unrated only
        </label>
        <span style={{ color: "var(--text-muted)" }}>
          {filteredSamples.length} samples
        </span>
      </div>

      {filteredSamples.length === 0 ? (
        <div
          style={{
            textAlign: "center",
            padding: 60,
            color: "var(--text-muted)",
          }}
        >
          {showOnlyUnrated
            ? "All samples in this filter are rated!"
            : "No samples match this filter."}
        </div>
      ) : currentSample ? (
        <>
          {/* Navigation */}
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              margin: "12px 0",
            }}
          >
            <button
              onClick={handlePrev}
              disabled={currentIdx === 0}
              style={{
                background: currentIdx === 0 ? "var(--border)" : "var(--bg-elevated)",
                color: currentIdx === 0 ? "var(--text-muted)" : "var(--text)",
                fontSize: 13,
              }}
            >
              Prev (A)
            </button>
            <span style={{ fontSize: 13, color: "var(--text-muted)" }}>
              {currentIdx + 1} of {filteredSamples.length}
              {ratings[currentSample.sample_id] && (
                <span style={{ color: "var(--green)", marginLeft: 8 }}>Rated</span>
              )}
            </span>
            <button
              onClick={handleNext}
              disabled={currentIdx === filteredSamples.length - 1}
              style={{
                background:
                  currentIdx === filteredSamples.length - 1 ? "var(--border)" : "var(--bg-elevated)",
                color:
                  currentIdx === filteredSamples.length - 1 ? "var(--text-muted)" : "var(--text)",
                fontSize: 13,
              }}
            >
              Next (D)
            </button>
          </div>

          {/* Sample card */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 2fr",
              gap: 16,
              marginBottom: 20,
              alignItems: "start",
            }}
          >
            {/* Task prompt */}
            <div
              style={{
                background: "var(--bg-card)",
                border: "1px solid var(--border)",
                borderRadius: "var(--radius)",
                padding: 20,
                position: "sticky",
                top: 20,
              }}
            >
              <div
                style={{
                  fontSize: 11,
                  color: "var(--text-muted)",
                  textTransform: "uppercase",
                  letterSpacing: 1,
                  marginBottom: 12,
                }}
              >
                Task Prompt
              </div>
              <div style={{ fontSize: 14, whiteSpace: "pre-wrap", lineHeight: 1.6 }}>
                {currentSample.task_prompt}
              </div>
              <div
                style={{
                  marginTop: 12,
                  fontSize: 11,
                  display: "flex",
                  gap: 8,
                }}
              >
                <span style={{
                  padding: "2px 8px",
                  borderRadius: 4,
                  background: {
                    code: "#dbeafe",
                    data_logic: "#fef3c7",
                    analysis: "#d1fae5",
                    writing: "#ede9fe",
                    creative: "#fce7f3",
                  }[currentSample.domain] || "var(--bg-elevated)",
                  color: {
                    code: "#1e40af",
                    data_logic: "#92400e",
                    analysis: "#065f46",
                    writing: "#5b21b6",
                    creative: "#9d174d",
                  }[currentSample.domain] || "var(--text-muted)",
                  fontWeight: 600,
                }}>
                  {currentSample.domain.replace("_", " ")}
                </span>
              </div>
            </div>

            {/* Output */}
            {(() => {
              const wordCount = currentSample.output.split(/\s+/).filter(Boolean).length;
              const isLong = wordCount > 600;
              // Collapsed view: show ~300 words worth of characters as a rough cut
              const COLLAPSE_CHARS = 1800;
              const showFull = !isLong || outputExpanded;
              return (
                <div
                  style={{
                    background: "var(--bg-card)",
                    border: "1px solid var(--border)",
                    borderRadius: "var(--radius)",
                    padding: 20,
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      marginBottom: 12,
                    }}
                  >
                    <span
                      style={{
                        fontSize: 11,
                        color: "var(--text-muted)",
                        textTransform: "uppercase",
                        letterSpacing: 1,
                      }}
                    >
                      Model Output
                    </span>
                    <span style={{ fontSize: 11, color: "var(--text-muted)" }}>
                      {wordCount} words{isLong && <span style={{ color: "#f59e0b", marginLeft: 6 }}>long output</span>}
                    </span>
                  </div>
                  <div style={{ fontSize: 14, whiteSpace: "pre-wrap", lineHeight: 1.6, position: "relative" }}>
                    {showFull
                      ? currentSample.output
                      : currentSample.output.slice(0, COLLAPSE_CHARS) + "..."}
                    {/* Fade gradient when collapsed */}
                    {isLong && !outputExpanded && (
                      <div style={{
                        position: "absolute",
                        bottom: 0,
                        left: 0,
                        right: 0,
                        height: 60,
                        background: "linear-gradient(transparent, var(--bg-card))",
                        pointerEvents: "none",
                      }} />
                    )}
                  </div>
                  {/* Error 4: long output expand/collapse toggle */}
                  {isLong && (
                    <button
                      onClick={() => setOutputExpanded((v) => !v)}
                      style={{
                        marginTop: 12,
                        background: "var(--bg-elevated)",
                        border: "1px solid var(--border)",
                        color: "var(--text-muted)",
                        fontSize: 12,
                        padding: "6px 12px",
                        borderRadius: "var(--radius)",
                        cursor: "pointer",
                        width: "100%",
                      }}
                    >
                      {outputExpanded ? "Collapse output" : `Show full output (${wordCount} words)`}
                    </button>
                  )}
                </div>
              );
            })()}
          </div>

          {/* Quick reference bar */}
          <div
            style={{
              display: "flex",
              gap: 2,
              marginBottom: 12,
              padding: "8px 12px",
              background: "var(--bg-card)",
              border: "1px solid var(--border)",
              borderRadius: "var(--radius)",
              fontSize: 11,
              justifyContent: "space-between",
            }}
          >
            {LEVELS.map((l) => (
              <span
                key={l.level}
                style={{
                  color: selectedLevel === l.level ? l.color : "var(--text-muted)",
                  fontWeight: selectedLevel === l.level ? 700 : 400,
                  cursor: "pointer",
                  transition: "all 0.15s",
                }}
                onClick={() => setSelectedLevel(l.level)}
              >
                {l.level}={l.label}
              </span>
            ))}
          </div>

          {/* Rating buttons */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr 1fr",
              gap: 8,
              marginBottom: 16,
            }}
          >
            {LEVELS.map((level) => (
              <RatingButton
                key={level.level}
                level={level}
                selected={selectedLevel === level.level}
                onClick={() => setSelectedLevel(level.level)}
              />
            ))}
          </div>

          {/* Rationale */}
          <div style={{ marginBottom: 16 }}>
            <textarea
              value={rationale}
              onChange={(e) => setRationale(e.target.value)}
              placeholder="Brief rationale (optional but helpful)"
              rows={2}
              style={{
                width: "100%",
                background: "var(--bg-elevated)",
                color: "var(--text)",
                border: "1px solid var(--border)",
                borderRadius: "var(--radius)",
                padding: "10px 12px",
                fontSize: 14,
                resize: "vertical",
                fontFamily: "inherit",
              }}
            />
          </div>

          {/* Submit */}
          <button
            onClick={handleSubmit}
            disabled={selectedLevel === null}
            style={{
              width: "100%",
              padding: 14,
              background: selectedLevel !== null ? "var(--accent)" : "var(--border)",
              color: selectedLevel !== null ? "#fff" : "var(--text-muted)",
              fontWeight: 600,
              fontSize: 15,
            }}
          >
            {ratings[currentSample.sample_id] ? "Update Rating" : "Submit Rating"} (Enter)
          </button>

          {/* Keyboard hint */}
          <p
            style={{
              textAlign: "center",
              fontSize: 12,
              color: "var(--text-muted)",
              marginTop: 10,
            }}
          >
            1-6 to select level, Enter to submit, A/D or arrows to navigate
          </p>
        </>
      ) : null}
    </div>
  );
}
