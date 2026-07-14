import os
import glob
from datetime import datetime

base_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"
domain = "https://sqgate.com" # Assuming sqgate.com or sqgate.online. User previously said sqgate.online in feedback. Let's use sqgate.online based on the feedback sheet!
domain = "https://sqgate.online"

# Find all HTML files
html_files = []
# Root pages
for f in glob.glob(os.path.join(base_dir, "*.html")):
    html_files.append(f)

# Blog pages
for f in glob.glob(os.path.join(base_dir, "blog", "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(base_dir, "blog", "posts", "*.html")):
    html_files.append(f)
# Tool pages
for f in glob.glob(os.path.join(base_dir, "circuit-simulator", "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(base_dir, "fsm", "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(base_dir, "k-map", "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(base_dir, "puzzle", "*.html")):
    html_files.append(f)

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

today = datetime.now().strftime("%Y-%m-%d")

for filepath in html_files:
    if "template" in filepath.lower():
        continue
        
    rel_path = os.path.relpath(filepath, base_dir).replace('\\', '/')
    if rel_path == "index.html":
        url = f"{domain}/"
        priority = "1.0"
    else:
        url = f"{domain}/{rel_path}"
        if rel_path.startswith("blog/posts/"):
            priority = "0.7"
        elif rel_path.startswith("blog/"):
            priority = "0.8"
        else:
            priority = "0.9"
            
    sitemap_content += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_content += "</urlset>"

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap.xml
"""
with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
    
print(f"Sitemap and robots.txt generated successfully for {len(html_files)} files.")
