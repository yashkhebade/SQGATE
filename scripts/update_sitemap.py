import os

blog_slugs = [
    "karnaugh-maps-intro",
    "fsm-design-javascript",
    "sequential-logic-demystified",
    "cmos-logic-gates",
    "from-schematic-to-verilog",
    "architecting-8bit-alu",
    "boolean-algebra-hacks",
    "multiplexers-demultiplexers"
]

sitemap_path = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\sitemap.xml"

with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

urls_to_add = ""
for slug in blog_slugs:
    urls_to_add += f"""
  <url>
    <loc>https://sqgate.online/blog/posts/{slug}.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""

# insert before </urlset>
insert_pos = sitemap_content.rfind("</urlset>")
if insert_pos != -1:
    new_sitemap = sitemap_content[:insert_pos] + urls_to_add + "\n" + sitemap_content[insert_pos:]
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(new_sitemap)
    print("Sitemap updated.")
else:
    print("Could not find </urlset> in sitemap.xml")
