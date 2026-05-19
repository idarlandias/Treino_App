# Treino App v2 — Design Spec

**Data:** 2026-05-18  
**Status:** Aprovado  
**Repo:** https://github.com/idarlandias/Treino_App  

---

## Contexto

O Treino App é uma web app de arquivo único (`index.html`) hospedada no GitHub Pages. O usuário é o próprio dono — usa no celular para marcar exercícios na academia. O progresso é salvo em `localStorage`.

**Problemas a resolver:**
1. Visual claro não tem a vibe de academia que o usuário quer
2. Navegação por barra horizontal no topo é pouco intuitiva no celular
3. Sem instalação como app (PWA)
4. Sem swipe entre dias
5. Progresso perdido se trocar de browser/dispositivo

---

## Decisões de Design

| Decisão | Escolha |
|---|---|
| Tema | Midnight Black (escuro estilo academia) |
| Cor de fundo principal | `#09090f` |
| Cor de cards/superfícies | `#12121e` |
| Cor de bordas | `#1a1a28` |
| Acento principal (Push) | `#5b9aff` (azul elétrico) |
| Acento Pull | `#00d4a0` (verde-água) |
| Acento Legs | `#a87fff` (roxo) |
| Acento Full Body | `#f06040` (laranja) |
| Acento sucesso | `#22c77e` (verde) |
| Navegação mobile | Bottom Tab Bar |
| Gestos | Swipe horizontal entre dias |
| Instalação | PWA (manifest + service worker) |
| Backend | Offline-first + servidor local opcional |
| Sync | Automático ao detectar servidor + toast de confirmação |

---

## Arquitetura

```
GitHub Pages                       PC do usuário (opcional)
┌─────────────────────┐            ┌──────────────────────┐
│  index.html (v2)    │──────────▶│  backend/server.js   │
│  manifest.json      │  fetch     │  (Express, porta 3001)│
│  sw.js              │◀──────────│  backend/treino.db   │
│  icons/             │  JSON      │  (SQLite)            │
└─────────────────────┘            └──────────────────────┘
        │
        └─ localStorage (fallback offline)
```

### Fluxo de dados

1. **Academia (offline):** exercícios marcados → `localStorage`
2. **Em casa — ao abrir o app:**
   - Detecta servidor → `GET /api/progresso/:weekKey`
   - Se retornar dado → carrega do servidor (sobrescreve localStorage local)
   - Se servidor offline → carrega localStorage normalmente
3. **Em casa — ao marcar exercício:**
   - Salva em `localStorage` (imediato, síncrono)
   - Se servidor disponível → `POST /api/progresso` (assíncrono)
   - Toast "✓ Progresso salvo no PC" após POST com sucesso
4. **Conflito:** servidor sempre é fonte de verdade. Dado local é descartado se servidor tiver estado mais recente para a semana atual.

---

## Frontend — `index.html` v2

### Dados preservados

O array `W` com todos os 7 dias × exercícios, incluindo séries, reps, descanso, técnica especial e links de GIF do Google Drive, **permanece intacto**. Nenhum dado de treino é alterado.

### Estrutura de telas

```
┌─ Status bar ─────────────────────┐
│ 09:42                    📶 🔋  │
├─ App header ──────────────────────┤
│ Treino          [● PC CONECTADO] │
│ ████████░░░░  3/7  2🔥           │  ← progress bar semanal
├─ Day panel (scrollável) ──────────┤
│ 💪 Segunda-feira  [A — PUSH]     │
│ [Marcar tudo]                    │
│                                  │
│ ✓ Supino Reto       5×10 1min   │  ← card done (strikethrough)
│ ✓ Supino Inclinado  4×10 45s    │
│ ▼ Cross Over        3×15 SLOW   │  ← card expandido
│   │ Séries │ Reps │ Descanso │  │
│   │   3   │  15  │   1min   │  │
│   └ [GIF demo]                  │
│ ○ Tríceps Testa     4×10 45s   │
│ ○ Pulley Corda      3×12 30s   │
│                                  │
├─ Toast (transitório) ─────────────┤
│ ✓ Progresso salvo no PC          │
├─ Bottom Tab Bar ───────────────────┤
│  💪    🏋️    🦵    💪    ···   │
│  SEG   TER   QUA   QUI   +3    │
│  ▬     ●                        │  ← ▬ = ativo, ● = completo
└───────────────────────────────────┘
```

### Bottom Tab Bar

- Exibe 5 tabs fixas: SEG, TER, QUA, QUI + botão `···` que abre um drawer com SEX, SÁB, DOM
- Tab ativa: background `rgba(91,154,255,.1)`, label azul `#5b9aff`, barra indicadora 14px embaixo
- Tab concluída: ícone emoji colorido (sem grayscale), label verde `#22c77e`
- Tab atual (hoje): borda sutil dourada `rgba(232,160,32,.3)`

### Swipe entre dias

- `touchstart` / `touchmove` / `touchend` no painel de conteúdo
- Threshold: 50px de deslocamento horizontal para mudar de dia
- Animação: `translateX` com `transition: transform .25s ease`
- Não interfere com scroll vertical

### Cards de exercício

- Estado padrão: fundo `#12121e`, borda `#1a1a28`
- Estado done: borda `rgba(34,199,126,.15)`, fundo com tint verde muito suave
- Estado expandido: borda `rgba(91,154,255,.25)`
- Tap no nome ou no botão `▼` expande/colapsa
- Expandido mostra: grid 3 células (Séries / Reps / Descanso) + GIF (lazy load, fallback se falhar)
- Checkbox tap: animação scale `1→1.15→1` em 200ms

### PWA

Arquivos novos na raiz:

**`manifest.json`**
```json
{
  "name": "Treino Semanal",
  "short_name": "Treino",
  "description": "Controle de treino semanal Push/Pull/Legs",
  "start_url": "/Treino_App/",
  "display": "standalone",
  "background_color": "#09090f",
  "theme_color": "#09090f",
  "orientation": "portrait",
  "icons": [
    { "src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

**`sw.js`** (service worker)
- Estratégia cache-first para assets estáticos (`index.html`, `manifest.json`, `sw.js`)
- Estratégia network-first para chamadas `localhost:3001/api/*` (não cacheadas)
- Cache name: `treino-v2`

**Ícones:** gerar PNG 192×192 e 512×512 com emoji 🏋️ em fundo `#09090f`

### Detecção de servidor

```js
async function detectServer() {
  try {
    const r = await fetch('http://localhost:3001/api/health', { signal: AbortSignal.timeout(2000) });
    return r.ok;
  } catch {
    return false;
  }
}
```

Chamado uma vez no load. Resultado salvo em variável `serverAvailable`. Badge no header mostra/oculta conforme resultado.

### Sincronização

```js
async function syncToServer(weekKey, state) {
  if (!serverAvailable) return;
  await fetch('http://localhost:3001/api/progresso', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ weekKey, state })
  });
  showToast('✓ Progresso salvo no PC');
}
```

Chamado após cada `toggleEx()` e `toggleDay()`.

### Toast

- Aparece 64px acima do bottom nav
- Fundo `#1a2a1a`, borda `rgba(34,199,126,.3)`, texto verde `#22c77e`
- Auto-desaparece após 2.5s com `opacity` transition

---

## Backend — `backend/`

### Estrutura

```
backend/
├── server.js       # Express server
├── db.js           # SQLite helpers (better-sqlite3)
├── package.json
└── treino.db       # criado automaticamente
```

### `package.json`

```json
{
  "name": "treino-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": { "start": "node server.js" },
  "dependencies": {
    "express": "^4.18.0",
    "better-sqlite3": "^9.0.0",
    "cors": "^2.8.5"
  }
}
```

### Schema SQLite

```sql
CREATE TABLE IF NOT EXISTS progresso (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  week_key   TEXT NOT NULL,
  state_json TEXT NOT NULL,          -- JSON do objeto S ({ "0_0": true, ... })
  updated_at TEXT DEFAULT (datetime('now'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_week ON progresso(week_key);
```

### Endpoints

| Método | Path | Descrição |
|---|---|---|
| GET | `/api/health` | Retorna `{ ok: true }` — usado para detecção |
| GET | `/api/progresso/:weekKey` | Retorna estado da semana |
| POST | `/api/progresso` | Upsert do estado (body: `{ weekKey, state }`) |
| DELETE | `/api/progresso/:weekKey` | Reset da semana |

### CORS

Liberar `http://localhost:*` e `https://idarlandias.github.io` para aceitar requests da GitHub Pages e do servidor local.

### Inicialização

```bash
cd backend
npm install
node server.js
# Server running on http://localhost:3001
```

---

## Arquivos modificados / criados

| Arquivo | Ação |
|---|---|
| `index.html` | Reescrito — mesmo dado `W`, novo visual/nav/PWA/sync |
| `manifest.json` | Novo |
| `sw.js` | Novo |
| `icons/icon-192.png` | Novo |
| `icons/icon-512.png` | Novo |
| `backend/server.js` | Novo |
| `backend/db.js` | Novo |
| `backend/package.json` | Novo |
| `.gitignore` | Atualizar: `backend/treino.db`, `backend/node_modules/` |

---

## O que NÃO muda

- Array `W` (todos os exercícios, séries, reps, descanso, técnicas)
- Links de GIF (`lh3.googleusercontent.com/d/{id}`)
- Fallback de GIF quebrado
- Lógica de `weekKey()` para identificar a semana atual
- Função `confetti()` ao completar um dia
- `resetWeek()` (mantida, agora também deleta no servidor se disponível)

---

## Critérios de sucesso

- [ ] App abre em `localhost` e no GitHub Pages com tema escuro
- [ ] Bottom nav mostra 5 dias + drawer com os outros 3
- [ ] Swipe horizontal muda de dia sem interferir com scroll vertical
- [ ] PWA instalável no Android/iOS (Chrome "Adicionar à tela inicial")
- [ ] App funciona 100% offline (sem `backend/`)
- [ ] Com `node backend/server.js` rodando, sincroniza e exibe toast
- [ ] Todos os GIFs carregam normalmente ou mostram fallback
- [ ] Confetti ao completar um dia ainda funciona
