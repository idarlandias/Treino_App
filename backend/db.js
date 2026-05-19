const initSqlJs = require('sql.js');
const fs = require('fs');
const path = require('path');

let db = null;

async function initDatabase() {
  const SQL = await initSqlJs();
  const dbPath = path.join(__dirname, 'treino.db');

  let data = null;
  if (fs.existsSync(dbPath)) {
    data = fs.readFileSync(dbPath);
  }

  db = new SQL.Database(data);

  db.run(`
    CREATE TABLE IF NOT EXISTS progresso (
      id         INTEGER PRIMARY KEY AUTOINCREMENT,
      week_key   TEXT NOT NULL UNIQUE,
      state_json TEXT NOT NULL,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);

  saveDatabase();
  return db;
}

function saveDatabase() {
  if (db) {
    const data = db.export();
    const buffer = Buffer.from(data);
    fs.writeFileSync(path.join(__dirname, 'treino.db'), buffer);
  }
}

function getProgresso(weekKey) {
  if (!db) throw new Error('Database not initialized');
  const stmt = db.prepare('SELECT state_json FROM progresso WHERE week_key = ?');
  stmt.bind([weekKey]);
  if (stmt.step()) {
    const row = stmt.getAsObject();
    stmt.free();
    return JSON.parse(row.state_json);
  }
  stmt.free();
  return null;
}

function upsertProgresso(weekKey, state) {
  if (!db) throw new Error('Database not initialized');
  db.run(
    `INSERT OR REPLACE INTO progresso (week_key, state_json, updated_at)
     VALUES (?, ?, CURRENT_TIMESTAMP)`,
    [weekKey, JSON.stringify(state)]
  );
  saveDatabase();
}

function deleteProgresso(weekKey) {
  if (!db) throw new Error('Database not initialized');
  db.run('DELETE FROM progresso WHERE week_key = ?', [weekKey]);
  saveDatabase();
}

module.exports = { initDatabase, getProgresso, upsertProgresso, deleteProgresso };
