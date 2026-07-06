const fs = require('fs');

let nid = 1;
function genId() { return 'g' + (nid++); }

function createProj(name, buildFunc) {
  nid = 1;
  const gates = [];
  const wires = [];
  
  function add(type, x, y, opts = {}) {
    const g = { id: genId(), type, x, y, value: opts.value || 0 };
    if (opts.cn) g.cn = opts.cn;
    gates.push(g);
    return g;
  }
  
  function wire(from, to, outIdx = 0, inIdx = 0) {
    wires.push({ from: from.id, outIdx, to: to.id, inIdx });
  }
  
  buildFunc(add, wire);
  
  const snap = { gates, wires, custom: [], nid };
  const jsonStr = JSON.stringify({ name, data: snap });
  // Escape for btoa like in browser:
  const encodedStr = encodeURIComponent(jsonStr).replace(/%([0-9A-F]{2})/g, (match, p1) => String.fromCharCode('0x' + p1));
  const b64 = Buffer.from(encodedStr, 'binary').toString('base64');
  return { name, b64 };
}

const templates = [
  {
    category: "Basic Logic & Arithmetic",
    items: [
      {
        title: "Half Adder",
        desc: "Adds two single-bit binary numbers, outputting a Sum and a Carry. Built using an XOR and an AND gate.",
        icon: "➕",
        proj: createProj("Half Adder", (add, wire) => {
          const a = add('sw', 100, 100);
          const b = add('sw', 100, 200);
          const xor = add('xor', 300, 100);
          const and = add('and', 300, 250);
          const sum = add('led', 500, 100);
          const carry = add('led', 500, 250);
          wire(a, xor, 0, 0); wire(a, and, 0, 0);
          wire(b, xor, 0, 1); wire(b, and, 0, 1);
          wire(xor, sum); wire(and, carry);
        })
      },
      {
        title: "Full Adder",
        desc: "Adds three bits (A, B, Carry-In) to produce a Sum and Carry-Out. Essential building block for CPUs.",
        icon: "🧮",
        proj: createProj("Full Adder", (add, wire) => {
          const a = add('sw', 100, 100);
          const b = add('sw', 100, 180);
          const cin = add('sw', 100, 260);
          const xor1 = add('xor', 250, 120);
          const xor2 = add('xor', 400, 160);
          const and1 = add('and', 250, 220);
          const and2 = add('and', 400, 260);
          const or1 = add('or', 550, 240);
          const sum = add('led', 550, 160);
          const cout = add('led', 700, 240);
          
          wire(a, xor1, 0, 0); wire(b, xor1, 0, 1);
          wire(xor1, xor2, 0, 0); wire(cin, xor2, 0, 1);
          wire(xor2, sum, 0, 0);
          
          wire(a, and1, 0, 0); wire(b, and1, 0, 1);
          wire(xor1, and2, 0, 0); wire(cin, and2, 0, 1);
          wire(and1, or1, 0, 0); wire(and2, or1, 0, 1);
          wire(or1, cout, 0, 0);
        })
      }
    ]
  },
  {
    category: "Flip-Flops & Memory",
    items: [
      {
        title: "SR Latch (NOR based)",
        desc: "The simplest form of memory, constructed using two cross-coupled NOR gates. Has Set and Reset inputs.",
        icon: "💾",
        proj: createProj("SR Latch (NOR)", (add, wire) => {
          const r = add('sw', 100, 100);
          const s = add('sw', 100, 250);
          const nor1 = add('nor', 300, 120);
          const nor2 = add('nor', 300, 230);
          const q = add('led', 500, 120);
          const qnot = add('led', 500, 230);
          
          wire(r, nor1, 0, 0);
          wire(s, nor2, 0, 1);
          wire(nor2, nor1, 0, 1); // cross-couple
          wire(nor1, nor2, 0, 0); // cross-couple
          wire(nor1, q, 0, 0);
          wire(nor2, qnot, 0, 0);
        })
      },
      {
        title: "D Flip-Flop",
        desc: "A data flip-flop that captures the value of the D-input at a definite portion of the clock cycle.",
        icon: "⏱️",
        proj: createProj("D Flip-Flop Circuit", (add, wire) => {
          const clk = add('clk', 100, 200, { freq: 1 });
          const d = add('sw', 100, 100);
          const dff = add('dff', 300, 150);
          const q = add('led', 500, 130);
          const qn = add('led', 500, 170);
          wire(d, dff, 0, 0);
          wire(clk, dff, 0, 1);
          wire(dff, q, 0, 0);
          wire(dff, qn, 1, 0);
        })
      }
    ]
  },
  {
    category: "Combinational Logic",
    items: [
      {
        title: "2-to-1 Multiplexer (MUX)",
        desc: "Selects between two input signals based on a selector bit and forwards the selected input to the output.",
        icon: "🔀",
        proj: createProj("2-to-1 MUX", (add, wire) => {
          const in0 = add('sw', 100, 100);
          const in1 = add('sw', 100, 300);
          const sel = add('sw', 100, 200);
          const not1 = add('not', 200, 150);
          const and1 = add('and', 350, 120);
          const and2 = add('and', 350, 280);
          const or1 = add('or', 500, 200);
          const out = add('led', 650, 200);
          
          wire(in0, and1, 0, 0);
          wire(sel, not1, 0, 0);
          wire(not1, and1, 0, 1);
          
          wire(in1, and2, 0, 1);
          wire(sel, and2, 0, 0);
          
          wire(and1, or1, 0, 0);
          wire(and2, or1, 0, 1);
          wire(or1, out, 0, 0);
        })
      }
    ]
  }
];

// Generate JS output
let output = `// Auto-generated Circuit Templates\n\nconst GALLERY_DATA = [\n`;
templates.forEach(cat => {
  output += `  {\n    category: ${JSON.stringify(cat.category)},\n    items: [\n`;
  cat.items.forEach(item => {
    output += `      {\n        title: ${JSON.stringify(item.title)},\n        desc: ${JSON.stringify(item.desc)},\n        icon: ${JSON.stringify(item.icon)},\n        url: "/home/#load=" + "${item.proj.b64}"\n      },\n`;
  });
  output += `    ]\n  },\n`;
});
output += `];\n\n`;

// Generate the script that will construct the UI
output += `
function initGallery() {
  const root = document.getElementById('gallery-root');
  if (!root) return;
  
  GALLERY_DATA.forEach(cat => {
    const sec = document.createElement('div');
    sec.className = 'category-section';
    
    const h2 = document.createElement('h2');
    h2.className = 'category-title';
    h2.textContent = cat.category;
    sec.appendChild(h2);
    
    const grid = document.createElement('div');
    grid.className = 'grid';
    
    cat.items.forEach(item => {
      const card = document.createElement('a');
      card.className = 'card';
      card.href = item.url;
      
      const thumb = document.createElement('div');
      thumb.className = 'card-thumb';
      const icon = document.createElement('div');
      icon.className = 'card-thumb-icon';
      icon.textContent = item.icon;
      thumb.appendChild(icon);
      
      const cont = document.createElement('div');
      cont.className = 'card-content';
      
      const title = document.createElement('h3');
      title.className = 'card-title';
      title.textContent = item.title;
      
      const desc = document.createElement('p');
      desc.className = 'card-desc';
      desc.textContent = item.desc;
      
      const btn = document.createElement('div');
      btn.className = 'card-btn';
      btn.innerHTML = 'Load Template <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>';
      
      cont.appendChild(title);
      cont.appendChild(desc);
      cont.appendChild(btn);
      
      card.appendChild(thumb);
      card.appendChild(cont);
      grid.appendChild(card);
    });
    
    sec.appendChild(grid);
    root.appendChild(sec);
  });
}

document.addEventListener('DOMContentLoaded', initGallery);
`;

fs.writeFileSync('C:/Users/Admin/.gemini/antigravity/worktrees/resilient-hertz/apply-code-changes/templates/app.js', output);
console.log('Successfully wrote templates/app.js');
