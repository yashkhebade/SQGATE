import os
import re
from datetime import datetime

today = datetime.utcnow().strftime("%Y-%m-%d")

# 1. Update sitemap.xml
urls = [
    ('/', 1.0, 'weekly'),
    ('/home/', 1.0, 'weekly'),
    ('/fsm/', 0.9, 'weekly'),
    ('/k-map/', 0.9, 'weekly'),
    ('/puzzle/', 0.8, 'weekly'),
    ('/circuit-simulator/', 0.8, 'weekly'),
    ('/truth-table-generator.html', 0.8, 'weekly'),
    ('/pricing.html', 0.6, 'monthly'),
    ('/contact.html', 0.5, 'monthly'),
    ('/privacy.html', 0.3, 'monthly'),
    ('/terms.html', 0.3, 'monthly'),
    ('/refund.html', 0.3, 'monthly')
]

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for loc, prio, freq in urls:
    sitemap_xml += f"""  <url>
    <loc>https://sqgate.online{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio:.1f}</priority>
  </url>\n"""
sitemap_xml += "</urlset>\n"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
print("Updated sitemap.xml")

# 2. JSON-LD Schemas
schemas = {
    'home/index.html': '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "SQGate",
    "url": "https://sqgate.online/home",
    "description": "Free browser-based digital electronics toolkit for simulating logic circuits, designing FSMs, and solving K-Maps.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }
  }
  </script>''',
    'fsm/index.html': '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "SQGate FSM Designer",
    "url": "https://sqgate.online/fsm",
    "description": "Design Finite State Machine diagrams interactively and export synthesizable Verilog HDL code.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>''',
    'k-map/index.html': '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "SQGate K-Map Solver",
    "url": "https://sqgate.online/k-map",
    "description": "Interactive Karnaugh Map solver for up to 6 variables with automatic grouping.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>''',
    'puzzle/index.html': '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "VideoGame",
    "name": "SQGate Logic Quest",
    "url": "https://sqgate.online/puzzle",
    "description": "Master logic gates by solving puzzles with restricted gate sets in this browser game.",
    "genre": "Educational Puzzle Game",
    "playMode": "SinglePlayer"
  }
  </script>'''
}

for filepath, schema in schemas.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Avoid double injection
        if "application/ld+json" not in content:
            # Inject right before </head>
            content = content.replace('</head>', schema + '\n</head>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected JSON-LD into {filepath}")
        else:
            print(f"JSON-LD already exists in {filepath}")

print("Done!")
