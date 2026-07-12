import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'icon.png' in content:
        # We might have href="icon.png" or src="icon.png" or src="/icon.png"
        content = content.replace('icon.png', 'icon.webp')
        
        # Revert the apple-touch-icon which might be required to be PNG (but we deleted the PNG anyway)
        # So we just keep it as webp for now, or maybe it doesn't matter.
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, _, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
