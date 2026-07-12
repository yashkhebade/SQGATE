import re

filepath = 'home/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Enhance #ed-topbar
content = re.sub(
    r'(#ed-topbar\{[^}]*background:rgba\(18,\s*18,\s*23,\s*0\.65\);[^}]*backdrop-filter:blur\([^)]*\);)([^}]*\})',
    r'\1 box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5); border-bottom: 1px solid rgba(255,255,255,0.08); \2',
    content
)
if 'backdrop-filter:blur(24px)' not in content:
    content = content.replace('backdrop-filter:blur(16px)', 'backdrop-filter:blur(24px)')

# Enhance .proj-action-btn and tb-btn hover
if '.tb-btn:hover{background:var(--bg3);color:var(--t1)}' in content:
    content = content.replace(
        '.tb-btn:hover{background:var(--bg3);color:var(--t1)}',
        '.tb-btn:hover{background:var(--bg3);color:var(--acc); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.3);}'
    )

# Inner shadow for canvas
if '#ed-canvas{flex:1;background:var(--bg0);' in content:
    content = content.replace(
        '#ed-canvas{flex:1;background:var(--bg0);',
        '#ed-canvas{flex:1;background:var(--bg0); box-shadow: inset 0 0 20px rgba(0,0,0,0.8); border-radius: 8px; margin: 4px; overflow: hidden; '
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched home/index.html")

# Same for circuit-simulator/index.html
filepath = 'circuit-simulator/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'(#ed-topbar\{[^}]*background:rgba\(18,\s*18,\s*23,\s*0\.65\);[^}]*backdrop-filter:blur\([^)]*\);)([^}]*\})',
    r'\1 box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5); border-bottom: 1px solid rgba(255,255,255,0.08); \2',
    content
)
content = content.replace('backdrop-filter:blur(16px)', 'backdrop-filter:blur(24px)')

if '.tb-btn:hover{background:var(--bg3);color:var(--t1)}' in content:
    content = content.replace(
        '.tb-btn:hover{background:var(--bg3);color:var(--t1)}',
        '.tb-btn:hover{background:var(--bg3);color:var(--acc); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.3);}'
    )

if '#ed-canvas{flex:1;background:var(--bg0);' in content:
    content = content.replace(
        '#ed-canvas{flex:1;background:var(--bg0);',
        '#ed-canvas{flex:1;background:var(--bg0); box-shadow: inset 0 0 20px rgba(0,0,0,0.8); border-radius: 8px; margin: 4px; overflow: hidden; '
    )
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched circuit-simulator/index.html")

