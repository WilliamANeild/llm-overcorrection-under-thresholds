import { put, list } from "@vercel/blob";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { rater_id, ratings } = body;

    if (!rater_id || !ratings || !Array.isArray(ratings)) {
      return NextResponse.json({ error: "Missing rater_id or ratings" }, { status: 400 });
    }

    const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
    const filename = `ratings/${rater_id}/${timestamp}.json`;

    const blob = await put(filename, JSON.stringify({ rater_id, ratings, submitted_at: timestamp }, null, 2), {
      contentType: "application/json",
      access: "public",
    });

    return NextResponse.json({ ok: true, url: blob.url, count: ratings.length });
  } catch (err) {
    console.error("Submit ratings error:", err);
    return NextResponse.json({ error: "Failed to save ratings" }, { status: 500 });
  }
}

export async function GET() {
  try {
    const { blobs } = await list({ prefix: "ratings/" });
    return NextResponse.json({ blobs: blobs.map((b) => ({ url: b.url, pathname: b.pathname, uploadedAt: b.uploadedAt })) });
  } catch (err) {
    console.error("List ratings error:", err);
    return NextResponse.json({ error: "Failed to list ratings" }, { status: 500 });
  }
}
