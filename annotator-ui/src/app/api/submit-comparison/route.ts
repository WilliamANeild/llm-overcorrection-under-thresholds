import { put } from "@vercel/blob";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { rater_id, choices, skipped } = body;

    if (!rater_id || !choices || !Array.isArray(choices)) {
      return NextResponse.json({ error: "Missing rater_id or choices" }, { status: 400 });
    }

    const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
    const filename = `comparisons/${rater_id}/${timestamp}.json`;

    const blob = await put(
      filename,
      JSON.stringify({ rater_id, choices, skipped: skipped || [], submitted_at: timestamp }, null, 2),
      { contentType: "application/json", access: "public" }
    );

    return NextResponse.json({ ok: true, url: blob.url, count: choices.length });
  } catch (err) {
    console.error("Submit comparison error:", err);
    return NextResponse.json({ error: "Failed to save comparison" }, { status: 500 });
  }
}
