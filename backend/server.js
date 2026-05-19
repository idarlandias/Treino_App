const express = require('express');
const cors = require('cors');
const { getProgresso, upsertProgresso, deleteProgresso } = require('./db');

const app = express();
const PORT = 3001;

app.use(cors({
  origin: [
    'https://idarlandias.github.io',
    /^http:\/\/localhost(:\d+)?$/
  ]
}));
app.use(express.json());

app.get('/api/health', (_req, res) => {
  res.json({ ok: true });
});

app.get('/api/progresso/:weekKey', (req, res) => {
  const state = getProgresso(req.params.weekKey);
  if (!state) return res.status(404).json({ error: 'not_found' });
  res.json({ weekKey: req.params.weekKey, state });
});

app.post('/api/progresso', (req, res) => {
  const { weekKey, state } = req.body;
  if (!weekKey || !state) return res.status(400).json({ error: 'weekKey and state required' });
  upsertProgresso(weekKey, state);
  res.json({ ok: true });
});

app.delete('/api/progresso/:weekKey', (req, res) => {
  deleteProgresso(req.params.weekKey);
  res.json({ ok: true });
});

app.listen(PORT, () => console.log(`Treino backend running on http://localhost:${PORT}`));
