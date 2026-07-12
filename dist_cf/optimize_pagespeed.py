import os
from PIL import Image

def convert_to_webp(filename):
    if not os.path.exists(filename):
        return
    img = Image.open(filename)
    webp_filename = filename.replace('.png', '.webp')
    img.save(webp_filename, 'webp', quality=85)
    print(f"Converted {filename} to {webp_filename}")
    
# 1. Convert Images
convert_to_webp('login_bg.png')
convert_to_webp('simulator_preview.png')
convert_to_webp('icon.png')

def optimize_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # Replace image references
    if 'login_bg.png' in content:
        content = content.replace('login_bg.png', 'login_bg.webp')
        changed = True
    if 'simulator_preview.png' in content:
        content = content.replace('simulator_preview.png', 'simulator_preview.webp')
        changed = True
    if 'icon.png' in content:
        # Don't replace icon.png in apple-touch-icon as it might require png, but do replace standard icon
        # Actually, let's just replace href="/icon.png" with href="/icon.webp"
        content = content.replace('href="/icon.png"', 'href="/icon.webp"')
        changed = True

    # Check for @import fonts
    if '@import url(\'https://fonts.googleapis.com' in content:
        # Find the specific font import
        import_str = None
        for line in content.split('\n'):
            if '@import url(\'https://fonts.googleapis.com' in line:
                import_str = line.strip()
                break
        
        if import_str:
            # Extract URL
            start = import_str.find("'") + 1
            end = import_str.find("'", start)
            url = import_str[start:end]
            
            # Replace @import with links
            links = f"""<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{url}">"""
            
            # Insert links right before </head> if possible, or just replace the line if it was in <style>
            # Actually the @imports were right after <head> in some files?
            # Let's see:
            # @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;700&display=swap');
            
            # Let's remove the @import and add the <link> tags just above </head>
            content = content.replace(import_str, '')
            content = content.replace('</head>', f'{links}\n</head>')
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Optimized {filepath}")

# 2. Update HTML files
for root, _, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            optimize_html(os.path.join(root, file))
