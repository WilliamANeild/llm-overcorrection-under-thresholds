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

type View = "login" | "annotate" | "review";

// ---- Rating scale ----

const LEVELS = [
  {
    level: 1,
    label: "Inadequate",
    desc: "Does not address the task, or so incorrect it must be restarted. A user could not build on this.",
    color: "#ef4444",
    key: "1",
  },
  {
    level: 2,
    label: "Incomplete",
    desc: "Addresses the right task but missing explicitly requested components. A user would have to add significant content.",
    color: "#f97316",
    key: "2",
  },
  {
    level: 3,
    label: "Functional",
    desc: "All requested components present, but clear weaknesses in accuracy, clarity, or tone. Usable with edits.",
    color: "#f59e0b",
    key: "3",
  },
  {
    level: 4,
    label: "Sufficient",
    desc: "All requested components present and executed competently. A reasonable user would accept without changes.",
    color: "#22c55e",
    key: "4",
  },
  {
    level: 5,
    label: "Polished",
    desc: "Well-executed with thoughtfulness beyond the minimum. Nothing to fix.",
    color: "#3b82f6",
    key: "5",
  },
  {
    level: 6,
    label: "Overdone",
    desc: "Adds unrequested complexity, excessive length, or drifted from the original ask. Would need to cut or refocus.",
    color: "#a855f7",
    key: "6",
  },
];

// ---- Storage helpers ----

function storageKey(raterId: string) {
  return `s3_ratings_${raterId}`;
}

function loadRatings(raterId: string): Record<string, Rating> {
  if (typeof window === "undefined") return {};
  const raw = localStorage.getItem(storageKey(raterId));
  return raw ? JSON.parse(raw) : {};
}

function saveRatings(raterId: string, ratings: Record<string, Rating>) {
  localStorage.setItem(storageKey(raterId), JSON.stringify(ratings));
}

// ---- Components ----

function ProgressBar({ done, total }: { done: number; total: number }) {
  const pct = total > 0 ? (done / total) * 100 : 0;
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
      <div
        style={{
          flex: 1,
          height: 8,
          background: "var(--bg-elevated)",
          borderRadius: 4,
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: `${pct}%`,
            height: "100%",
            background: pct === 100 ? "var(--green)" : "var(--accent)",
            transition: "width 0.3s ease",
          }}
        />
      </div>
      <span style={{ color: "var(--text-muted)", fontSize: 13, whiteSpace: "nowrap" }}>
        {done} / {total}
      </span>
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
        background: selected ? `${level.color}18` : "var(--bg-elevated)",
        border: `2px solid ${selected ? level.color : "var(--border)"}`,
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
        }}
      >
        {level.level}
      </span>
      <div>
        <div style={{ fontWeight: 600, marginBottom: 2 }}>
          {level.label}
          <span style={{ color: "var(--text-muted)", fontWeight: 400, fontSize: 12, marginLeft: 8 }}>
            press {level.key}
          </span>
        </div>
        <div style={{ fontSize: 13, color: "var(--text-muted)", lineHeight: 1.4 }}>
          {level.desc}
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
  const [loginError, setLoginError] = useState("");

  // Auto-fetch samples and assignments on mount
  useEffect(() => {
    Promise.all([
      fetch("/samples.json").then((r) => (r.ok ? r.json() : [])),
      fetch("/assignments.json").then((r) => (r.ok ? r.json() : null)),
    ])
      .then(([samplesData, assignmentsData]) => {
        setAllSamples(samplesData as Sample[]);
        setAssignments(assignmentsData as Assignments | null);
        setLoading(false);
      })
      .catch(() => {
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

    setSamples(assignedSamples);
    const saved = loadRatings(id);
    setRatings(saved);

    // Jump to first unrated
    const firstUnrated = assignedSamples.findIndex((s) => !saved[s.sample_id]);
    setCurrentIdx(firstUnrated >= 0 ? firstUnrated : 0);
    setRaterId(id);
    setView("annotate");
  }, [raterId, allSamples, assignments]);

  // Load existing rating when navigating
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
    saveRatings(raterId, newRatings);
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

  const handleExport = () => {
    const ratingsList = Object.values(ratings);
    const header = "sample_id,level,rationale,timestamp,rater_id\n";
    const csvRows = ratingsList
      .map(
        (r) =>
          `"${r.sample_id}",${r.level},"${r.rationale.replace(/"/g, '""')}","${r.timestamp}","${raterId}"`
      )
      .join("\n");
    const csv = header + csvRows;
    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ratings_${raterId}_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleExportJSON = () => {
    const ratingsList = Object.values(ratings).map((r) => ({
      ...r,
      rater_id: raterId,
    }));
    const blob = new Blob([JSON.stringify(ratingsList, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ratings_${raterId}_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // ---- LOGIN VIEW ----
  if (view === "login") {
    return (
      <div style={{ maxWidth: 480, margin: "80px auto", padding: "0 20px" }}>
        <h1 style={{ fontSize: 24, marginBottom: 8 }}>Study 3 Annotator</h1>
        <p style={{ color: "var(--text-muted)", marginBottom: 32 }}>
          Human evaluation for judge calibration (Phase 0)
        </p>

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

            {allSamples.length === 0 && (
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
            <button onClick={handleExport} style={{ background: "var(--accent)", color: "#fff" }}>
              Export CSV
            </button>
            <button onClick={handleExportJSON} style={{ background: "var(--green)", color: "#fff" }}>
              Export JSON
            </button>
          </div>
        </div>

        <p style={{ color: "var(--text-muted)", marginBottom: 24 }}>
          {ratingsList.length} of {samples.length} rated as {raterId}
        </p>

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
                  const level = LEVELS.find((l) => l.level === r.level)!;
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

  // ---- ANNOTATE VIEW ----
  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "20px" }}>
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
            Review
          </button>
          <button
            onClick={handleExport}
            style={{ background: "var(--accent)", color: "#fff", fontSize: 13 }}
          >
            Export
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
              gridTemplateColumns: "1fr 1fr",
              gap: 16,
              marginBottom: 20,
            }}
          >
            {/* Task prompt */}
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
                  color: "var(--text-muted)",
                  display: "flex",
                  gap: 12,
                }}
              >
                <span>Domain: {currentSample.domain}</span>
                <span>Turn: {currentSample.turn}</span>
              </div>
            </div>

            {/* Output */}
            <div
              style={{
                background: "var(--bg-card)",
                border: "1px solid var(--border)",
                borderRadius: "var(--radius)",
                padding: 20,
                maxHeight: 400,
                overflowY: "auto",
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
                Model Output
              </div>
              <div style={{ fontSize: 14, whiteSpace: "pre-wrap", lineHeight: 1.6 }}>
                {currentSample.output}
              </div>
            </div>
          </div>

          {/* Rating buttons */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
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
