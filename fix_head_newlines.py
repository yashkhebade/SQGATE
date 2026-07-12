import os

def fix_head(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<head>\\n  <meta charset="UTF-8" />' in content:
        new_content = content.replace('<head>\\n  <meta charset="UTF-8" />', '<head>\n  <meta charset="UTF-8" />')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root, _, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            fix_head(os.path.join(root, file))
