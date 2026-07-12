#!/usr/bin/env node
// ═══════════════════════════════════════════════════════════════════
// SQGATE EDA — Gate Test Suite
// Tests every gate type in calcGate with multiple input combinations
// Run:  node test_gates.js
// ═══════════════════════════════════════════════════════════════════

'use strict';

// ── calcGate: exact replica from main.html lines 2612-2733 ──
function calcGate(gate, ins) {
  const t = gate.type;
  const i = function(n) { return ins[n] !== undefined ? (ins[n] ? 1 : 0) : 0; };
  switch (t) {
    case 'input':  return [gate.value ? 1 : 0];
    case 'clock':  return [gate.value ? 1 : 0];
    case 'const0': return [0];
    case 'const1': return [1];
    case 'buffer': return [i(0)];
    case 'and':    return [i(0) & i(1)];
    case 'or':     return [i(0) | i(1)];
    case 'not':    return [i(0) ? 0 : 1];
    case 'nand':   return [(i(0) & i(1)) ? 0 : 1];
    case 'nor':    return [(i(0) | i(1)) ? 0 : 1];
    case 'xor':    return [i(0) ^ i(1)];
    case 'xnor':   return [(i(0) ^ i(1)) ? 0 : 1];
    case 'output': return [];
    case 'led':    return [];
    case 'seg7':   return [];
    case 'hexdisp':return [];
    case 'merge4': return [(i(0)<<3) | (i(1)<<2) | (i(2)<<1) | i(3)];
    case 'split4': { const v = ins[0] || 0; return [(v>>3)&1, (v>>2)&1, (v>>1)&1, v&1]; }
    case 'merge8': return [(i(0)<<7)|(i(1)<<6)|(i(2)<<5)|(i(3)<<4)|(i(4)<<3)|(i(5)<<2)|(i(6)<<1)|i(7)];
    case 'split8': { const v = ins[0] || 0; return [(v>>7)&1,(v>>6)&1,(v>>5)&1,(v>>4)&1,(v>>3)&1,(v>>2)&1,(v>>1)&1,v&1]; }
    case 'rom8': {
      if (!gate.mem) gate.mem = new Uint8Array(256);
      return [gate.mem[ins[0] || 0]];
    }
    case 'ram8': {
      const clk = i(3);
      if (!gate.mem) gate.mem = new Uint8Array(256);
      const addr = ins[0] || 0;
      if (clk && !gate.prevClk) {
        if (i(2)) gate.mem[addr] = ins[1] || 0;
      }
      gate.prevClk = clk;
      return [gate.mem[addr]];
    }
    case 'alu8': {
      const a = ins[0] || 0, b = ins[1] || 0, op = ins[2] || 0;
      let y = 0, c = 0;
      switch (op) {
        case 0: y = a + b; c = (y > 255) ? 1 : 0; break;
        case 1: y = a - b; c = (y < 0) ? 1 : 0; break;
        case 2: y = a & b; break;
        case 3: y = a | b; break;
        case 4: y = a ^ b; break;
        case 5: y = a << 1; c = (a >> 7) & 1; break;
        case 6: y = a >> 1; c = a & 1; break;
        case 7: y = (~a) & 255; break;
      }
      y = y & 255;
      return [y, c, (y === 0) ? 1 : 0];
    }
    case 'count8': {
      const clk = i(0);
      if (!gate.q) gate.q = 0;
      if (i(2)) gate.q = 0;
      else if (clk && !gate.prevClk) {
        if (i(1)) {
          if (i(3)) gate.q = (gate.q + 1) & 255;
          else gate.q = (gate.q - 1) & 255;
        }
      }
      gate.prevClk = clk;
      const tc = (i(3) && gate.q === 255) || (!i(3) && gate.q === 0);
      return [gate.q, tc ? 1 : 0];
    }
    case 'shift8': {
      const clk = i(0);
      if (!gate.q) gate.q = 0;
      if (clk && !gate.prevClk) {
        if (i(1)) gate.q = ins[2] || 0;
        else gate.q = ((gate.q << 1) | i(3)) & 255;
      }
      gate.prevClk = clk;
      return [gate.q, (gate.q >> 7) & 1];
    }
    case 'ha': { const s = i(0) ^ i(1), c = i(0) & i(1); return [s, c]; }
    case 'fa': { const s = i(0) ^ i(1) ^ i(2), c = (i(0) & i(1)) | (i(1) & i(2)) | (i(0) & i(2)); return [s, c]; }
    case 'add4': {
      const A = (i(0)<<3)|(i(1)<<2)|(i(2)<<1)|i(3);
      const B = (i(4)<<3)|(i(5)<<2)|(i(6)<<1)|i(7);
      const r = A + B + i(8);
      return [(r>>3)&1, (r>>2)&1, (r>>1)&1, r&1, r > 15 ? 1 : 0];
    }
    case 'mux2': return [i(2) ? i(1) : i(0)];
    case 'mux4': { const sel = (i(5)<<1)|i(4); return [i(sel)]; }
    case 'dmux2': return [i(1) ? 0 : i(0), i(1) ? i(0) : 0];
    case 'dmux4': { const sel = (i(2)<<1)|i(1), o = [0,0,0,0]; o[sel] = i(0); return o; }
    case 'enc4': { if(i(3)) return[1,1]; if(i(2)) return[0,1]; if(i(1)) return[1,0]; return[0,0]; }
    case 'dec2': { const sel = (i(1)<<1)|i(0), o = [0,0,0,0]; o[sel] = 1; return o; }
    case 'sr': {
      if (i(0) && i(1)) { gate.fault = true; return [gate.q ? 1 : 0, gate.q ? 0 : 1]; }
      gate.fault = false;
      if (i(0)) gate.q = 1; else if (i(1)) gate.q = 0;
      return [gate.q ? 1 : 0, gate.q ? 0 : 1];
    }
    case 'dlatch': { if (i(1)) gate.q = i(0); return [gate.q ? 1 : 0, gate.q ? 0 : 1]; }
    case 'dff': {
      const clk = i(1);
      if (i(2)) gate.q = 0; else if (clk && !gate.prevClk) gate.q = i(0);
      gate.prevClk = clk; return [gate.q ? 1 : 0, gate.q ? 0 : 1];
    }
    case 'jkff': {
      const clk = i(2);
      if (clk && !gate.prevClk) {
        if (i(0) && i(1)) gate.q = gate.q ? 0 : 1;
        else if (i(0)) gate.q = 1; else if (i(1)) gate.q = 0;
      }
      gate.prevClk = clk; return [gate.q ? 1 : 0, gate.q ? 0 : 1];
    }
    case 'tff': {
      const clk = i(1);
      if (clk && !gate.prevClk && i(0)) gate.q = gate.q ? 0 : 1;
      gate.prevClk = clk; return [gate.q ? 1 : 0, gate.q ? 0 : 1];
    }
    default: return [0];
  }
}

// ═══════════════════════════════════════════════════════════════
// Test helpers
// ═══════════════════════════════════════════════════════════════
let totalPass = 0, totalFail = 0;

function arrEq(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
  return true;
}

function test(name, gate, ins, expected) {
  const result = calcGate(gate, ins);
  if (arrEq(result, expected)) {
    totalPass++;
    return true;
  } else {
    totalFail++;
    console.log(`  FAIL: ${name}  ins=${JSON.stringify(ins)}  expected=${JSON.stringify(expected)}  got=${JSON.stringify(result)}`);
    return false;
  }
}

function section(name) {
  process.stdout.write(`  Testing ${name}... `);
}
function sectionEnd(count) {
  console.log(`${count} cases OK`);
}

// Helper: clock rising edge — sets prevClk=0 then calls with clk=1
function risingEdge(gate, ins) {
  // Ensure prevClk is 0 before the rising edge
  gate.prevClk = 0;
  return calcGate(gate, ins);
}

// ═══════════════════════════════════════════════════════════════
// Tests begin
// ═══════════════════════════════════════════════════════════════
console.log('\n╔══════════════════════════════════════════════════════╗');
console.log('║  SQGATE EDA — Comprehensive Gate Test Suite        ║');
console.log('╚══════════════════════════════════════════════════════╝\n');

// ── 1. INPUT ──
(function() {
  section('input');
  let c = 0;
  test('input-0', { type: 'input', value: 0 }, [], [0]) && c++;
  test('input-1', { type: 'input', value: 1 }, [], [1]) && c++;
  test('input-falsy', { type: 'input', value: null }, [], [0]) && c++;
  test('input-truthy', { type: 'input', value: 5 }, [], [1]) && c++;
  sectionEnd(c);
})();

// ── 2. CLOCK ──
(function() {
  section('clock');
  let c = 0;
  test('clock-0', { type: 'clock', value: 0 }, [], [0]) && c++;
  test('clock-1', { type: 'clock', value: 1 }, [], [1]) && c++;
  sectionEnd(c);
})();

// ── 3. CONST0 ──
(function() {
  section('const0');
  let c = 0;
  test('const0', { type: 'const0' }, [], [0]) && c++;
  test('const0-ignored-inputs', { type: 'const0' }, [1, 1], [0]) && c++;
  sectionEnd(c);
})();

// ── 4. CONST1 ──
(function() {
  section('const1');
  let c = 0;
  test('const1', { type: 'const1' }, [], [1]) && c++;
  test('const1-ignored-inputs', { type: 'const1' }, [0, 0], [1]) && c++;
  sectionEnd(c);
})();

// ── 5. BUFFER ──
(function() {
  section('buffer');
  let c = 0;
  test('buffer-0', { type: 'buffer' }, [0], [0]) && c++;
  test('buffer-1', { type: 'buffer' }, [1], [1]) && c++;
  test('buffer-undef', { type: 'buffer' }, [], [0]) && c++;
  sectionEnd(c);
})();

// ── 6. AND — exhaustive 2-input truth table ──
(function() {
  section('and');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`and-${a}${b}`, { type: 'and' }, [a, b], [a & b]) && c++;
  sectionEnd(c);
})();

// ── 7. OR — exhaustive ──
(function() {
  section('or');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`or-${a}${b}`, { type: 'or' }, [a, b], [a | b]) && c++;
  sectionEnd(c);
})();

// ── 8. NOT ──
(function() {
  section('not');
  let c = 0;
  test('not-0', { type: 'not' }, [0], [1]) && c++;
  test('not-1', { type: 'not' }, [1], [0]) && c++;
  sectionEnd(c);
})();

// ── 9. NAND — exhaustive ──
(function() {
  section('nand');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`nand-${a}${b}`, { type: 'nand' }, [a, b], [(a & b) ? 0 : 1]) && c++;
  sectionEnd(c);
})();

// ── 10. NOR — exhaustive ──
(function() {
  section('nor');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`nor-${a}${b}`, { type: 'nor' }, [a, b], [(a | b) ? 0 : 1]) && c++;
  sectionEnd(c);
})();

// ── 11. XOR — exhaustive ──
(function() {
  section('xor');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`xor-${a}${b}`, { type: 'xor' }, [a, b], [a ^ b]) && c++;
  sectionEnd(c);
})();

// ── 12. XNOR — exhaustive ──
(function() {
  section('xnor');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      test(`xnor-${a}${b}`, { type: 'xnor' }, [a, b], [(a ^ b) ? 0 : 1]) && c++;
  sectionEnd(c);
})();

// ── 13. OUTPUT, LED, SEG7, HEXDISP — no outputs ──
(function() {
  section('output/led/seg7/hexdisp');
  let c = 0;
  test('output', { type: 'output' }, [1], []) && c++;
  test('led', { type: 'led' }, [1], []) && c++;
  test('seg7', { type: 'seg7' }, [1,0,1,0,1,0,1], []) && c++;
  test('hexdisp', { type: 'hexdisp' }, [10], []) && c++;
  sectionEnd(c);
})();

// ── 14. HALF ADDER — exhaustive ──
(function() {
  section('ha (half adder)');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++) {
      const sum = a ^ b, carry = a & b;
      test(`ha-${a}${b}`, { type: 'ha' }, [a, b], [sum, carry]) && c++;
    }
  sectionEnd(c);
})();

// ── 15. FULL ADDER — exhaustive ──
(function() {
  section('fa (full adder)');
  let c = 0;
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      for (let ci = 0; ci <= 1; ci++) {
        const sum = a ^ b ^ ci;
        const co = (a & b) | (b & ci) | (a & ci);
        test(`fa-${a}${b}${ci}`, { type: 'fa' }, [a, b, ci], [sum, co]) && c++;
      }
  sectionEnd(c);
})();

// ── 16. ADD4 — selected cases ──
(function() {
  section('add4 (4-bit adder)');
  let c = 0;
  // Helper to convert 4-bit number to array of bits [MSB..LSB]
  function bits4(n) { return [(n>>3)&1, (n>>2)&1, (n>>1)&1, n&1]; }
  
  const cases = [
    [0, 0, 0],   // 0+0+0
    [1, 1, 0],   // 1+1
    [7, 8, 0],   // 7+8=15
    [15, 0, 0],  // 15+0
    [15, 1, 0],  // 15+1=16 => overflow
    [15, 15, 0], // 15+15=30 => overflow
    [15, 15, 1], // 15+15+1=31 => overflow
    [0, 0, 1],   // 0+0+1
    [5, 3, 0],   // 5+3=8
    [8, 8, 1],   // 8+8+1=17 => overflow
  ];
  for (const [A, B, ci] of cases) {
    const r = A + B + ci;
    const expected = [(r>>3)&1, (r>>2)&1, (r>>1)&1, r&1, r > 15 ? 1 : 0];
    const ins = [...bits4(A), ...bits4(B), ci];
    test(`add4-${A}+${B}+${ci}`, { type: 'add4' }, ins, expected) && c++;
  }
  sectionEnd(c);
})();

// ── 17. MUX2 ──
(function() {
  section('mux2');
  let c = 0;
  // MUX2: ins = [A, B, S], out = S?B:A
  for (let a = 0; a <= 1; a++)
    for (let b = 0; b <= 1; b++)
      for (let s = 0; s <= 1; s++)
        test(`mux2-A${a}B${b}S${s}`, { type: 'mux2' }, [a, b, s], [s ? b : a]) && c++;
  sectionEnd(c);
})();

// ── 18. MUX4 ──
(function() {
  section('mux4');
  let c = 0;
  // MUX4: ins = [D0, D1, D2, D3, S0, S1], sel = (S1<<1)|S0
  const d = [1, 0, 1, 0]; // D0=1, D1=0, D2=1, D3=0
  for (let s1 = 0; s1 <= 1; s1++)
    for (let s0 = 0; s0 <= 1; s0++) {
      const sel = (s1 << 1) | s0;
      test(`mux4-sel${sel}`, { type: 'mux4' }, [...d, s0, s1], [d[sel]]) && c++;
    }
  // All inputs high
  test('mux4-allHi', { type: 'mux4' }, [1, 1, 1, 1, 0, 0], [1]) && c++;
  test('mux4-allLo', { type: 'mux4' }, [0, 0, 0, 0, 1, 1], [0]) && c++;
  sectionEnd(c);
})();

// ── 19. DMUX2 ──
(function() {
  section('dmux2');
  let c = 0;
  // DMUX2: ins = [IN, S], out = [S?0:IN, S?IN:0]
  for (let inp = 0; inp <= 1; inp++)
    for (let s = 0; s <= 1; s++)
      test(`dmux2-IN${inp}S${s}`, { type: 'dmux2' }, [inp, s], [s ? 0 : inp, s ? inp : 0]) && c++;
  sectionEnd(c);
})();

// ── 20. DMUX4 ──
(function() {
  section('dmux4');
  let c = 0;
  // DMUX4: ins = [IN, S0, S1], sel = (S1<<1)|S0, o[sel]=IN
  for (let s1 = 0; s1 <= 1; s1++)
    for (let s0 = 0; s0 <= 1; s0++) {
      const sel = (s1 << 1) | s0;
      const exp = [0, 0, 0, 0]; exp[sel] = 1;
      test(`dmux4-sel${sel}-IN1`, { type: 'dmux4' }, [1, s0, s1], exp) && c++;
      test(`dmux4-sel${sel}-IN0`, { type: 'dmux4' }, [0, s0, s1], [0,0,0,0]) && c++;
    }
  sectionEnd(c);
})();

// ── 21. ENC4 (4:2 priority encoder) ──
(function() {
  section('enc4');
  let c = 0;
  // Priority: I3 > I2 > I1 > I0
  test('enc4-none',    { type: 'enc4' }, [0,0,0,0], [0,0]) && c++;
  test('enc4-I0',      { type: 'enc4' }, [1,0,0,0], [0,0]) && c++;
  test('enc4-I1',      { type: 'enc4' }, [0,1,0,0], [1,0]) && c++;
  test('enc4-I2',      { type: 'enc4' }, [0,0,1,0], [0,1]) && c++;
  test('enc4-I3',      { type: 'enc4' }, [0,0,0,1], [1,1]) && c++;
  test('enc4-I2+I1',   { type: 'enc4' }, [0,1,1,0], [0,1]) && c++; // I2 wins
  test('enc4-I3+I1',   { type: 'enc4' }, [0,1,0,1], [1,1]) && c++; // I3 wins
  test('enc4-all',     { type: 'enc4' }, [1,1,1,1], [1,1]) && c++; // I3 wins
  sectionEnd(c);
})();

// ── 22. DEC2 (2:4 decoder) ──
(function() {
  section('dec2');
  let c = 0;
  // DEC2: ins = [A0, A1], sel = (A1<<1)|A0, o[sel]=1
  for (let a1 = 0; a1 <= 1; a1++)
    for (let a0 = 0; a0 <= 1; a0++) {
      const sel = (a1 << 1) | a0;
      const exp = [0, 0, 0, 0]; exp[sel] = 1;
      test(`dec2-${a1}${a0}`, { type: 'dec2' }, [a0, a1], exp) && c++;
    }
  sectionEnd(c);
})();

// ── 23. SR LATCH ──
(function() {
  section('sr (SR latch)');
  let c = 0;
  let gate = { type: 'sr', q: 0 };
  // Initial state: S=0, R=0 → hold (Q=0)
  test('sr-hold-0', gate, [0, 0], [0, 1]) && c++;
  // Set: S=1, R=0 → Q=1
  test('sr-set', gate, [1, 0], [1, 0]) && c++;
  // Hold after set: S=0, R=0 → Q=1
  test('sr-hold-1', gate, [0, 0], [1, 0]) && c++;
  // Reset: S=0, R=1 → Q=0
  test('sr-reset', gate, [0, 1], [0, 1]) && c++;
  // Hold after reset
  test('sr-hold-0b', gate, [0, 0], [0, 1]) && c++;
  // Invalid: S=1, R=1 → fault, holds previous Q
  test('sr-invalid', gate, [1, 1], [0, 1]) && c++;
  if (gate.fault !== true) { totalFail++; console.log('  FAIL: sr fault flag not set'); } else { c++; totalPass++; }
  sectionEnd(c);
})();

// ── 24. D LATCH ──
(function() {
  section('dlatch');
  let c = 0;
  let gate = { type: 'dlatch', q: 0 };
  // E=0 → hold
  test('dlatch-hold', gate, [1, 0], [0, 1]) && c++;
  // E=1, D=1 → transparent, Q=1
  test('dlatch-pass-1', gate, [1, 1], [1, 0]) && c++;
  // E=1, D=0 → transparent, Q=0
  test('dlatch-pass-0', gate, [0, 1], [0, 1]) && c++;
  // E=0 → hold (Q=0)
  test('dlatch-hold-0', gate, [1, 0], [0, 1]) && c++;
  // E=1, D=1 → latch open
  test('dlatch-reopen', gate, [1, 1], [1, 0]) && c++;
  // E=0 → hold Q=1
  test('dlatch-hold-1', gate, [0, 0], [1, 0]) && c++;
  sectionEnd(c);
})();

// ── 25. D FLIP-FLOP ──
(function() {
  section('dff');
  let c = 0;
  let gate = { type: 'dff', q: 0, prevClk: 0 };
  // No rising edge (clk=0): hold
  test('dff-hold', gate, [1, 0, 0], [0, 1]) && c++;
  // Rising edge with D=1: capture
  gate.prevClk = 0;
  test('dff-rise-d1', gate, [1, 1, 0], [1, 0]) && c++;
  // Clk stays high — no capture (D=0 shouldn't matter)
  test('dff-hold-hi', gate, [0, 1, 0], [1, 0]) && c++;
  // Clk goes low
  test('dff-low', gate, [0, 0, 0], [1, 0]) && c++;
  // Rising edge with D=0: capture 0
  test('dff-rise-d0', gate, [0, 1, 0], [0, 1]) && c++;
  // Reset
  gate.q = 1;
  test('dff-reset', gate, [1, 1, 1], [0, 1]) && c++;
  sectionEnd(c);
})();

// ── 26. JK FLIP-FLOP ──
(function() {
  section('jkff');
  let c = 0;
  let gate = { type: 'jkff', q: 0, prevClk: 0 };
  // J=0,K=0 → hold
  gate.prevClk = 0;
  test('jkff-hold', gate, [0, 0, 1], [0, 1]) && c++;
  // J=1,K=0 → set (rising edge)
  gate.prevClk = 0;
  test('jkff-set', gate, [1, 0, 1], [1, 0]) && c++;
  // J=0,K=1 → reset
  gate.prevClk = 0;
  test('jkff-reset', gate, [0, 1, 1], [0, 1]) && c++;
  // J=1,K=1 → toggle (Q was 0, becomes 1)
  gate.prevClk = 0;
  test('jkff-toggle-0to1', gate, [1, 1, 1], [1, 0]) && c++;
  // J=1,K=1 → toggle again (Q was 1, becomes 0)
  gate.prevClk = 0;
  test('jkff-toggle-1to0', gate, [1, 1, 1], [0, 1]) && c++;
  // No rising edge → hold
  test('jkff-no-edge', gate, [1, 0, 1], [0, 1]) && c++;
  sectionEnd(c);
})();

// ── 27. T FLIP-FLOP ──
(function() {
  section('tff');
  let c = 0;
  let gate = { type: 'tff', q: 0, prevClk: 0 };
  // T=0, rising edge → hold
  gate.prevClk = 0;
  test('tff-hold', gate, [0, 1], [0, 1]) && c++;
  // T=1, rising edge → toggle (0→1)
  gate.prevClk = 0;
  test('tff-toggle-0to1', gate, [1, 1], [1, 0]) && c++;
  // T=1, rising edge → toggle (1→0)
  gate.prevClk = 0;
  test('tff-toggle-1to0', gate, [1, 1], [0, 1]) && c++;
  // T=1, no edge (clk stays high) → hold
  test('tff-no-edge', gate, [1, 1], [0, 1]) && c++;
  // T=1, clk goes low → hold
  test('tff-clk-low', gate, [1, 0], [0, 1]) && c++;
  // T=1, rising edge again → toggle
  test('tff-toggle-again', gate, [1, 1], [1, 0]) && c++;
  sectionEnd(c);
})();

// ── 28. MERGE4 ──
(function() {
  section('merge4');
  let c = 0;
  test('merge4-0000', { type: 'merge4' }, [0,0,0,0], [0]) && c++;
  test('merge4-1111', { type: 'merge4' }, [1,1,1,1], [15]) && c++;
  test('merge4-1000', { type: 'merge4' }, [1,0,0,0], [8]) && c++;
  test('merge4-0001', { type: 'merge4' }, [0,0,0,1], [1]) && c++;
  test('merge4-0110', { type: 'merge4' }, [0,1,1,0], [6]) && c++;
  test('merge4-1010', { type: 'merge4' }, [1,0,1,0], [10]) && c++;
  sectionEnd(c);
})();

// ── 29. SPLIT4 ──
(function() {
  section('split4');
  let c = 0;
  test('split4-0',  { type: 'split4' }, [0],  [0,0,0,0]) && c++;
  test('split4-15', { type: 'split4' }, [15], [1,1,1,1]) && c++;
  test('split4-8',  { type: 'split4' }, [8],  [1,0,0,0]) && c++;
  test('split4-1',  { type: 'split4' }, [1],  [0,0,0,1]) && c++;
  test('split4-6',  { type: 'split4' }, [6],  [0,1,1,0]) && c++;
  test('split4-10', { type: 'split4' }, [10], [1,0,1,0]) && c++;
  sectionEnd(c);
})();

// ── 30. MERGE8 ──
(function() {
  section('merge8');
  let c = 0;
  test('merge8-all0', { type: 'merge8' }, [0,0,0,0,0,0,0,0], [0]) && c++;
  test('merge8-all1', { type: 'merge8' }, [1,1,1,1,1,1,1,1], [255]) && c++;
  test('merge8-128',  { type: 'merge8' }, [1,0,0,0,0,0,0,0], [128]) && c++;
  test('merge8-1',    { type: 'merge8' }, [0,0,0,0,0,0,0,1], [1]) && c++;
  test('merge8-170',  { type: 'merge8' }, [1,0,1,0,1,0,1,0], [170]) && c++;
  test('merge8-85',   { type: 'merge8' }, [0,1,0,1,0,1,0,1], [85]) && c++;
  sectionEnd(c);
})();

// ── 31. SPLIT8 ──
(function() {
  section('split8');
  let c = 0;
  test('split8-0',   { type: 'split8' }, [0],   [0,0,0,0,0,0,0,0]) && c++;
  test('split8-255', { type: 'split8' }, [255], [1,1,1,1,1,1,1,1]) && c++;
  test('split8-128', { type: 'split8' }, [128], [1,0,0,0,0,0,0,0]) && c++;
  test('split8-1',   { type: 'split8' }, [1],   [0,0,0,0,0,0,0,1]) && c++;
  test('split8-170', { type: 'split8' }, [170], [1,0,1,0,1,0,1,0]) && c++;
  test('split8-85',  { type: 'split8' }, [85],  [0,1,0,1,0,1,0,1]) && c++;
  sectionEnd(c);
})();

// ── 32. MERGE4/SPLIT4 roundtrip ──
(function() {
  section('merge4↔split4 roundtrip');
  let c = 0;
  for (let v = 0; v < 16; v++) {
    const bits = [(v>>3)&1, (v>>2)&1, (v>>1)&1, v&1];
    const merged = calcGate({ type: 'merge4' }, bits);
    const split  = calcGate({ type: 'split4' }, merged);
    if (arrEq(split, bits)) { totalPass++; c++; }
    else { totalFail++; console.log(`  FAIL: roundtrip4 v=${v}`); }
  }
  sectionEnd(c);
})();

// ── 33. MERGE8/SPLIT8 roundtrip ──
(function() {
  section('merge8↔split8 roundtrip');
  let c = 0;
  for (let v = 0; v < 256; v += 17) {  // sample every 17th to keep output sane
    const bits = [];
    for (let b = 7; b >= 0; b--) bits.push((v >> b) & 1);
    const merged = calcGate({ type: 'merge8' }, bits);
    const split  = calcGate({ type: 'split8' }, merged);
    if (arrEq(split, bits)) { totalPass++; c++; }
    else { totalFail++; console.log(`  FAIL: roundtrip8 v=${v}`); }
  }
  sectionEnd(c);
})();

// ── 34. ROM8 ──
(function() {
  section('rom8');
  let c = 0;
  const gate = { type: 'rom8' };
  // Empty ROM reads 0
  test('rom8-empty', gate, [0], [0]) && c++;
  test('rom8-empty-42', gate, [42], [0]) && c++;
  // Write data manually and read back
  gate.mem = new Uint8Array(256);
  gate.mem[0] = 0xAB;
  gate.mem[10] = 0xFF;
  gate.mem[255] = 0x42;
  test('rom8-read-0', gate, [0], [0xAB]) && c++;
  test('rom8-read-10', gate, [10], [0xFF]) && c++;
  test('rom8-read-255', gate, [255], [0x42]) && c++;
  test('rom8-read-1', gate, [1], [0]) && c++;
  sectionEnd(c);
})();

// ── 35. RAM8 ──
(function() {
  section('ram8');
  let c = 0;
  // ins: [addr, din, we, clk]
  const gate = { type: 'ram8', prevClk: 0 };
  
  // Read empty → 0
  test('ram8-empty', gate, [0, 0, 0, 0], [0]) && c++;
  
  // Write: addr=5, din=0xAA, we=1, rising edge
  gate.prevClk = 0;
  test('ram8-write', gate, [5, 0xAA, 1, 1], [0xAA]) && c++;
  
  // Read back with clk low
  test('ram8-readback', gate, [5, 0, 0, 0], [0xAA]) && c++;
  
  // Read another address → 0
  test('ram8-read-other', gate, [6, 0, 0, 0], [0]) && c++;
  
  // WE=0 on rising edge → no write
  gate.prevClk = 0;
  test('ram8-no-write', gate, [6, 0xBB, 0, 1], [0]) && c++;
  test('ram8-verify-no-write', gate, [6, 0, 0, 0], [0]) && c++;
  
  // Write to addr=6
  gate.prevClk = 0;
  test('ram8-write-6', gate, [6, 0x55, 1, 1], [0x55]) && c++;
  
  // Verify addr=5 unchanged
  test('ram8-addr5-unchanged', gate, [5, 0, 0, 0], [0xAA]) && c++;
  sectionEnd(c);
})();

// ── 36. ALU8 ──
(function() {
  section('alu8');
  let c = 0;
  // ins: [A, B, OP] → [Y, Cout, Z]
  
  // OP=0: ADD
  test('alu8-add-10+20', { type: 'alu8' }, [10, 20, 0], [30, 0, 0]) && c++;
  test('alu8-add-200+100', { type: 'alu8' }, [200, 100, 0], [44, 1, 0]) && c++; // overflow
  test('alu8-add-0+0', { type: 'alu8' }, [0, 0, 0], [0, 0, 1]) && c++;  // zero flag
  
  // OP=1: SUB
  test('alu8-sub-30-10', { type: 'alu8' }, [30, 10, 1], [20, 0, 0]) && c++;
  test('alu8-sub-10-30', { type: 'alu8' }, [10, 30, 1], [236, 1, 0]) && c++; // underflow: -20 & 255 = 236
  test('alu8-sub-5-5', { type: 'alu8' }, [5, 5, 1], [0, 0, 1]) && c++;  // zero
  
  // OP=2: AND
  test('alu8-and', { type: 'alu8' }, [0xAA, 0x55, 2], [0x00, 0, 1]) && c++;
  test('alu8-and-ff', { type: 'alu8' }, [0xFF, 0xAA, 2], [0xAA, 0, 0]) && c++;
  
  // OP=3: OR
  test('alu8-or', { type: 'alu8' }, [0xAA, 0x55, 3], [0xFF, 0, 0]) && c++;
  test('alu8-or-00', { type: 'alu8' }, [0x00, 0x00, 3], [0x00, 0, 1]) && c++;
  
  // OP=4: XOR
  test('alu8-xor', { type: 'alu8' }, [0xFF, 0xFF, 4], [0x00, 0, 1]) && c++;
  test('alu8-xor-2', { type: 'alu8' }, [0xAA, 0x55, 4], [0xFF, 0, 0]) && c++;
  
  // OP=5: SHL
  test('alu8-shl-1', { type: 'alu8' }, [0x01, 0, 5], [0x02, 0, 0]) && c++;
  test('alu8-shl-80', { type: 'alu8' }, [0x80, 0, 5], [0x00, 1, 1]) && c++; // bit7 shifted out
  test('alu8-shl-c1', { type: 'alu8' }, [0xC1, 0, 5], [0x82, 1, 0]) && c++;
  
  // OP=6: SHR
  test('alu8-shr-02', { type: 'alu8' }, [0x02, 0, 6], [0x01, 0, 0]) && c++;
  test('alu8-shr-01', { type: 'alu8' }, [0x01, 0, 6], [0x00, 1, 1]) && c++; // bit0 shifted out, zero
  test('alu8-shr-ff', { type: 'alu8' }, [0xFF, 0, 6], [0x7F, 1, 0]) && c++;
  
  // OP=7: NOT
  test('alu8-not-00', { type: 'alu8' }, [0x00, 0, 7], [0xFF, 0, 0]) && c++;
  test('alu8-not-ff', { type: 'alu8' }, [0xFF, 0, 7], [0x00, 0, 1]) && c++;
  test('alu8-not-aa', { type: 'alu8' }, [0xAA, 0, 7], [0x55, 0, 0]) && c++;
  sectionEnd(c);
})();

// ── 37. COUNT8 ──
(function() {
  section('count8');
  let c = 0;
  // ins: [CLK, EN, CLR, UP]
  let gate = { type: 'count8', q: 0, prevClk: 0 };
  
  // Initial: Q=0, TC=1 (UP=0 → down mode, Q=0 → TC)
  test('count8-initial', gate, [0, 0, 0, 0], [0, 1]) && c++;
  
  // Count up: EN=1, UP=1, rising edge
  gate.prevClk = 0;
  test('count8-up1', gate, [1, 1, 0, 1], [1, 0]) && c++;
  gate.prevClk = 0;
  test('count8-up2', gate, [1, 1, 0, 1], [2, 0]) && c++;
  
  // No edge: hold
  test('count8-hold', gate, [1, 1, 0, 1], [2, 0]) && c++;
  
  // CLR
  test('count8-clear', gate, [0, 0, 1, 0], [0, 1]) && c++;
  
  // Count to 255 and check TC
  gate.q = 254; gate.prevClk = 0;
  test('count8-to-255', gate, [1, 1, 0, 1], [255, 1]) && c++;
  
  // Wrap around
  gate.prevClk = 0;
  test('count8-wrap', gate, [1, 1, 0, 1], [0, 0]) && c++;
  
  // Count down
  gate.q = 1; gate.prevClk = 0;
  test('count8-down', gate, [1, 1, 0, 0], [0, 1]) && c++;
  
  // EN=0 → don't count
  gate.q = 5; gate.prevClk = 0;
  test('count8-disabled', gate, [1, 0, 0, 1], [5, 0]) && c++;
  sectionEnd(c);
})();

// ── 38. SHIFT8 ──
(function() {
  section('shift8');
  let c = 0;
  // ins: [CLK, LD, Din, Sin]
  let gate = { type: 'shift8', q: 0, prevClk: 0 };
  
  // Load: LD=1, Din=0xA5, rising edge
  gate.prevClk = 0;
  test('shift8-load', gate, [1, 1, 0xA5, 0], [0xA5, 1]) && c++;
  
  // Shift left with Sin=0
  gate.prevClk = 0;
  test('shift8-shl-0', gate, [1, 0, 0, 0], [0x4A, 0]) && c++; // 0xA5<<1 = 0x14A & 255 = 0x4A
  
  // Shift left with Sin=1
  gate.prevClk = 0;
  test('shift8-shl-1', gate, [1, 0, 0, 1], [0x95, 1]) && c++; // 0x4A<<1|1 = 0x95
  
  // No edge → hold
  test('shift8-hold', gate, [1, 0, 0, 0], [0x95, 1]) && c++;
  
  // Clk low → hold
  test('shift8-low', gate, [0, 0, 0, 0], [0x95, 1]) && c++;
  
  // Load 0
  gate.prevClk = 0;
  test('shift8-load-0', gate, [1, 1, 0, 0], [0, 0]) && c++;
  sectionEnd(c);
})();

// ── 39. Comprehensive ADD4 — exhaustive for small values ──
(function() {
  section('add4 exhaustive (0-7 + 0-7)');
  let c = 0;
  function bits4(n) { return [(n>>3)&1, (n>>2)&1, (n>>1)&1, n&1]; }
  for (let a = 0; a < 8; a++)
    for (let b = 0; b < 8; b++) {
      const r = a + b;
      const expected = [(r>>3)&1, (r>>2)&1, (r>>1)&1, r&1, r > 15 ? 1 : 0];
      const ins = [...bits4(a), ...bits4(b), 0];
      test(`add4-${a}+${b}`, { type: 'add4' }, ins, expected) && c++;
    }
  sectionEnd(c);
})();

// ── 40. Edge cases: undefined/null inputs ──
(function() {
  section('edge cases (undefined inputs)');
  let c = 0;
  test('and-undef', { type: 'and' }, [undefined, undefined], [0]) && c++;
  test('or-undef', { type: 'or' }, [undefined, undefined], [0]) && c++;
  test('not-undef', { type: 'not' }, [undefined], [1]) && c++;
  test('xor-undef', { type: 'xor' }, [undefined, 1], [1]) && c++;
  test('buffer-undef', { type: 'buffer' }, [undefined], [0]) && c++;
  test('and-empty', { type: 'and' }, [], [0]) && c++;
  test('or-empty', { type: 'or' }, [], [0]) && c++;
  sectionEnd(c);
})();

// ── 41. Default/unknown gate type ──
(function() {
  section('unknown gate type');
  let c = 0;
  test('unknown', { type: 'foobar' }, [1, 1], [0]) && c++;
  test('empty-type', { type: '' }, [1], [0]) && c++;
  sectionEnd(c);
})();

// ═══════════════════════════════════════════════════════════════
// Summary
// ═══════════════════════════════════════════════════════════════
console.log('\n' + '─'.repeat(56));
console.log(`  Total: ${totalPass + totalFail}   Pass: ${totalPass}   Fail: ${totalFail}`);
if (totalFail === 0) {
  console.log('  ✅ ALL TESTS PASSED');
} else {
  console.log('  ❌ SOME TESTS FAILED');
}
console.log('─'.repeat(56) + '\n');

process.exit(totalFail > 0 ? 1 : 0);
