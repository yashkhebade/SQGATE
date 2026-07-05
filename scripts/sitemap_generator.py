import os
import urllib.parse
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://sqgate.online"
SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")

# Directories/files to exclude from sitemap
EXCLUDES = [
    "blog/template.html",
    "README.md",
    "node_modules",
    "components",
    ".git",
    "scripts",
    "dist_cf",
    "academo",
    "cedar-ls",
    "circuitverse",
    "falstad",
    "fsm-designer.html",
    "karnaugh-map-solver.html",
    "logic-gate-online",
    "logic-quest.html",
    "logicly",
    "logigator",
    "logisim",
    "simulator-io",
    "tinkercad",
    "truth-table-generator.html",
    "truth-table-tools",
    "verilog-simulator.html",
    "google1e701d9c9d06ac46.html"
]

def generate_sitemap():
    urls = []
    
    for root, dirs, files in os.walk(ROOT_DIR):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDES and not d.startswith('.')]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                # Check exclude list
                if any(excl in filepath for excl in EXCLUDES):
                    continue
                    
                # Compute relative path
                rel_path = os.path.relpath(filepath, ROOT_DIR)
                rel_path = rel_path.replace("\\", "/") # Normalize for URL
                
                # Strip index.html or .html to match canonical URLs
                if rel_path == "index.html" or rel_path == "home/index.html":
                    rel_path = ""
                elif rel_path.endswith("/index.html"):
                    rel_path = rel_path[:-10]  # keep the trailing slash
                elif rel_path.endswith(".html"):
                    rel_path = rel_path[:-5]
                
                # Default changefreq and priority
                changefreq = "monthly"
                priority = "0.6"
                
                # Adjust for important pages
                if rel_path == "":
                    priority = "1.0"
                    changefreq = "weekly"
                elif "blog/posts" in rel_path:
                    priority = "0.8"
                    changefreq = "monthly"
                elif "truth-table-generator" in rel_path or "logic-gates-sandbox" in rel_path:
                    priority = "0.9"
                    changefreq = "monthly"
                    
                url = f"{BASE_URL}/{rel_path}"
                
                urls.append({
                    "loc": url,
                    "lastmod": datetime.now().strftime("%Y-%m-%d"),
                    "changefreq": changefreq,
                    "priority": priority
                })
                
    # Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for u in urls:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{u['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        xml_lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        xml_lines.append(f"    <priority>{u['priority']}</priority>")
        xml_lines.append("  </url>")
        
    xml_lines.append("</urlset>")
    
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(xml_lines))
        
    print(f"Generated sitemap.xml with {len(urls)} entries at {SITEMAP_PATH}")

if __name__ == "__main__":
    generate_sitemap()
