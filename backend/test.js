// Node 18+ built-in fetch required
const BASE = 'http://localhost:3001';
const TEST_WEEK = 'test_2099_w1';

async function run() {
  let passed = 0;
  let failed = 0;

  async function check(label, fn) {
    try {
      await fn();
      console.log(`  ✓ ${label}`);
      passed++;
    } catch (e) {
      console.error(`  ✗ ${label}: ${e.message}`);
      failed++;
    }
  }

  function assert(condition, msg) {
    if (!condition) throw new Error(msg);
  }

  console.log('Running backend smoke tests...\n');

  await check('GET /api/health returns ok:true', async () => {
    const r = await fetch(`${BASE}/api/health`);
    const body = await r.json();
    assert(r.ok, `status ${r.status}`);
    assert(body.ok === true, `expected ok:true, got ${JSON.stringify(body)}`);
  });

  await check('GET /api/progresso/:weekKey returns 404 for unknown week', async () => {
    const r = await fetch(`${BASE}/api/progresso/${TEST_WEEK}`);
    assert(r.status === 404, `expected 404, got ${r.status}`);
  });

  await check('POST /api/progresso saves state', async () => {
    const state = { '0_0': true, '0_1': false };
    const r = await fetch(`${BASE}/api/progresso`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ weekKey: TEST_WEEK, state })
    });
    const body = await r.json();
    assert(r.ok, `status ${r.status}`);
    assert(body.ok === true, `expected ok:true`);
  });

  await check('GET /api/progresso/:weekKey returns saved state', async () => {
    const r = await fetch(`${BASE}/api/progresso/${TEST_WEEK}`);
    const body = await r.json();
    assert(r.ok, `status ${r.status}`);
    assert(body.state['0_0'] === true, `expected 0_0:true`);
  });

  await check('POST /api/progresso upserts (overwrites) existing week', async () => {
    const newState = { '0_0': false, '1_0': true };
    await fetch(`${BASE}/api/progresso`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ weekKey: TEST_WEEK, state: newState })
    });
    const r = await fetch(`${BASE}/api/progresso/${TEST_WEEK}`);
    const body = await r.json();
    assert(body.state['1_0'] === true, 'expected updated state');
    assert(body.state['0_0'] === false, 'expected overwritten value');
  });

  await check('DELETE /api/progresso/:weekKey removes state', async () => {
    await fetch(`${BASE}/api/progresso/${TEST_WEEK}`, { method: 'DELETE' });
    const r = await fetch(`${BASE}/api/progresso/${TEST_WEEK}`);
    assert(r.status === 404, `expected 404 after delete, got ${r.status}`);
  });

  console.log(`\n${passed} passed, ${failed} failed`);
  if (failed > 0) process.exit(1);
}

run().catch(e => { console.error(e); process.exit(1); });
