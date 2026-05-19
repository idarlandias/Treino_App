const Database = require('better-sqlite3');
const path = require('path');

const db = new Database(path.join(__dirname, 'treino.db'));

db.exec(`
  CREATE TABLE IF NOT EXISTS progresso (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    week_key   TEXT NOT NULL,
    state_json TEXT NOT NULL,
    updated_at TEXT DEFAULT (datetime('now'))
  );
  CREATE UNIQUE INDEX IF NOT EXISTS idx_week ON progresso(week_key);
`);

function getProgresso(weekKey) {
  const row = db.prepare('SELECT state_json FROM progresso WHERE week_key = ?').get(weekKey);
  return row ? JSON.parse(row.state_json) : null;
}

function upsertProgresso(weekKey, state) {
  db.prepare(`
    INSERT INTO progresso (week_key, state_json, updated_at)
    VALUES (?, ?, datetime('now'))
    ON CONFLICT(week_key) DO UPDATE SET
      state_json = excluded.state_json,
      updated_at = excluded.updated_at
  `).run(weekKey, JSON.stringify(state));
}

function deleteProgresso(weekKey) {
  db.prepare('DELETE FROM progresso WHERE week_key = ?').run(weekKey);
}

module.exports = { getProgresso, upsertProgresso, deleteProgresso };
