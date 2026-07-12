import re

filepath = 'home/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject CSS
css_injection = """
/* ── MOBILE UI REDESIGN ── */
@media (max-width: 768px) {
  #sidebar {
    position: absolute;
    top: 0; bottom: 0; left: 0;
    z-index: 1000;
    width: 250px !important;
    transform: translateX(0);
    transition: transform 0.3s var(--ease);
    box-shadow: 0 0 40px rgba(0,0,0,0.8);
    border-right: 1px solid var(--b2);
  }
  #sidebar.off {
    transform: translateX(-100%);
    width: 250px !important;
  }

  #rp {
    position: absolute;
    top: 0; bottom: 0; right: 0;
    z-index: 1000;
    width: 250px !important;
    transform: translateX(0);
    transition: transform 0.3s var(--ease);
    box-shadow: 0 0 40px rgba(0,0,0,0.8);
    border-left: 1px solid var(--b2);
  }
  #rp.off {
    transform: translateX(100%);
    width: 250px !important;
  }

  .tb-btn, .tb-btn-text, .tb-btn-primary, .step-btn {
    min-height: 44px;
    min-width: 44px;
  }
  
  #ed-topbar {
    overflow-x: auto;
    padding-left: 8px;
    padding-right: 16px;
  }
  #ed-topbar::-webkit-scrollbar { display: none; }
  
  /* Make touch target for canvas wires slightly bigger if possible, but standard is fine */
}
</style>
"""

content = content.replace('</style>', css_injection, 1)

# 2. Inject JS to close sidebars on mobile load
js_injection = """
// MOBILE INIT
if (window.innerWidth <= 768) {
  document.getElementById('sidebar').classList.add('off');
  document.getElementById('rp').classList.add('off');
}
"""

# Find a good place to inject the JS, e.g. at the end of the script where event listeners are added
# Let's just put it before the final </script>
content = content.replace('</script>\n</body>', js_injection + '\n</script>\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched home/index.html")
