import re
import os

filepath = 'fsm/index.html'
if not os.path.exists(filepath):
    print("FSM not found")
    exit()

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject CSS for Mobile Layout & UI Polish
css_injection = """
/* ── UI POLISH & MOBILE REDESIGN ── */
#fsm-header {
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(24px);
}
.tb-btn:hover {
  background: var(--bg3);
  color: var(--acc);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.tb-btn.active {
  color: var(--acc) !important;
  text-shadow: 0 0 10px var(--acc-glow);
  box-shadow: inset 0 0 10px rgba(62,187,242,0.1);
}
#fsm-canvas-wrap {
  box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
  border-radius: 8px;
  margin: 4px;
  overflow: hidden;
}

#btn-rp-fsm { display: none; }

@media (max-width: 768px) {
  #fsm-app { display: flex; flex-direction: column; overflow: hidden; }
  
  /* Right panel becomes a slide-out */
  #fsm-panel {
    position: absolute;
    right: 0; top: 46px; bottom: 0;
    width: 280px;
    z-index: 100;
    transform: translateX(0);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: -4px 0 24px rgba(0,0,0,0.5);
  }
  #fsm-panel.off {
    transform: translateX(100%);
  }
  
  #btn-rp-fsm {
    display: flex;
    background: none; border: 1px solid var(--b1); color: var(--t2);
    border-radius: var(--radius); padding: 4px 8px; font-size: 12px; cursor: pointer;
  }
  
  /* Enlarge Toolbar targets */
  .tb-btn { min-width: 44px; min-height: 44px; }
  #fsm-toolbar { overflow-x: auto; padding-bottom: 4px; }
}
"""

if '/* ── UI POLISH' not in content:
    # Insert before </head>
    content = content.replace('</head>', f'<style>{css_injection}</style>\n</head>')

# 2. Add Mobile Toggle Button to Header
toggle_btn = """
    <button id="btn-rp-fsm" onclick="document.getElementById('fsm-panel').classList.toggle('off')">
      <i class="ti ti-adjustments-alt"></i> Props
    </button>
"""
if 'btn-rp-fsm' not in content:
    # Add it to tb-group-right in fsm-header
    content = content.replace('<div class="tb-group-right">', f'<div class="tb-group-right">{toggle_btn}')

# 3. Add .off class to fsm-panel in JS on mobile load
js_init = """
<script>
// MOBILE INIT
if (window.innerWidth <= 768) {
  var rp = document.getElementById('fsm-panel');
  if(rp) rp.classList.add('off');
}
</script>
</body>
"""
if 'MOBILE INIT' not in content:
    content = content.replace('</body>', js_init)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("FSM patched successfully!")
