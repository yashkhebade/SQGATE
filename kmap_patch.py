import os

filepath = 'k-map/index.html'
if not os.path.exists(filepath):
    print("K-map not found")
    exit()

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

css_injection = """
/* ── UI POLISH & MOBILE REDESIGN ── */
.km-header {
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(24px);
}
@media (max-width: 768px) {
  .km-body {
    flex-direction: column !important;
    overflow-y: auto;
  }
  .km-panel-left, .km-panel-right {
    width: 100% !important;
    border-right: none !important;
    border-bottom: 1px solid var(--b1);
    min-height: auto;
  }
  .var-btn {
    min-width: 44px; min-height: 44px; font-size: 14px;
  }
}
"""

if '/* ── UI POLISH' not in content:
    content = content.replace('</head>', f'<style>{css_injection}</style>\n</head>')
    
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("K-Map patched successfully!")
