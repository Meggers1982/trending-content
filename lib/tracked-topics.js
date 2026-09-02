import { neon } from "@neondatabase/serverless";
import { slugifyTopic } from "@/lib/radar-profiles";

const sql = neon(process.env.DATABASE_URL);

function toEntry(row) {
  return {
    id: row.id,
    topic: row.topic,
    profile: row.profile,
    geo: row.geo,
    created_at: row.created_at instanceof Date ? row.created_at.toISOString() : row.created_at,
    last_scanned_at: row.last_scanned_at instanceof Date ? row.last_scanned_at.toISOString() : row.last_scanned_at
  };
}

export async function readTrackedTopics() {
  const rows = await sql`
    select id, topic, profile, geo, created_at, last_scanned_at
    from tracked_topics
    order by created_at asc
  `;
  return rows.map(toEntry);
}

export async function getTrackedTopic(id) {
  const rows = await sql`
    select id, topic, profile, geo, created_at, last_scanned_at
    from tracked_topics
    where id = ${id}
  `;
  return rows[0] ? toEntry(rows[0]) : null;
}

export async function addTrackedTopic({ topic, profile, geo }) {
  const id = slugifyTopic(topic);
  const existing = await getTrackedTopic(id);
  if (existing) {
    return { ok: false, message: "This topic is already tracked." };
  }
  const rows = await sql`
    insert into tracked_topics (id, topic, profile, geo)
    values (${id}, ${topic}, ${profile}, ${geo})
    returning id, topic, profile, geo, created_at, last_scanned_at
  `;
  return { ok: true, entry: toEntry(rows[0]) };
}

export async function removeTrackedTopic(id) {
  const rows = await sql`delete from tracked_topics where id = ${id} returning id`;
  if (rows.length === 0) {
    return { ok: false, message: "Tracked topic not found." };
  }
  return { ok: true };
}
