import os
import glob
import re

base_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"

# 1. Update internal links site-wide
# We want to replace href="/k-map/" with href="/k-map"
# href="/fsm/" -> href="/fsm"
# href="/puzzle/" -> href="/puzzle"
# href="/circuit-simulator/" -> href="/circuit-simulator"
# href="/truth-table-generator/" -> href="/truth-table-generator"
# href="/index.html" -> href="/"
# href="/terms.html" -> href="/terms"

replacements = {
    'href="/k-map/"': 'href="/k-map"',
    'href="/fsm/"': 'href="/fsm"',
    'href="/puzzle/"': 'href="/puzzle"',
    'href="/circuit-simulator/"': 'href="/circuit-simulator"',
    'href="/truth-table-generator/"': 'href="/truth-table-generator"',
    'href="/index.html"': 'href="/"',
    'href="/terms.html"': 'href="/terms"',
    'href="/privacy.html"': 'href="/privacy"',
    'href="/refund.html"': 'href="/refund"',
    'href="/blog/"': 'href="/blog"'
}

all_html = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

for file_path in all_html:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Standardize canonical links
    # Match <link rel="canonical" href="https://sqgate.online/something/"> and remove trailing slash
    # Match <link rel="canonical" href="https://sqgate.online/something.html"> and remove .html
    
    # We use regex to find the canonical tag and fix it
    def fix_canonical(match):
        url = match.group(1)
        if url != "https://sqgate.online/" and url.endswith("/"):
            url = url[:-1]
        if url.endswith(".html"):
            url = url[:-5]
        return f'<link rel="canonical" href="{url}">'

    content = re.sub(r'<link rel="canonical" href="(.*?)">', fix_canonical, content)
    
    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated links in {os.path.relpath(file_path, base_dir)}")

# We should also update terms.html, privacy.html, refund.html dates
legal_files = ["terms.html", "privacy.html", "refund.html"]
for file in legal_files:
    file_path = os.path.join(base_dir, file)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("Last Updated: June 2024", "Last Updated: July 2026")
        content = content.replace("Last Updated: January 2024", "Last Updated: July 2026")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated date in {file}")

print("Done standardizing internal links and canonicals.")
