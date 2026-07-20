import os
import re

base_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\posts"

redirects = {
    "intro-to-k-maps.html": "how-to-solve-karnaugh-maps.html",
    "3-karnaugh-maps.html": "how-to-solve-karnaugh-maps.html",
    "multiplexer-routing.html": "mastering-multiplexers-alu-design.html",
    "2-universal-gates.html": "understanding-nand-gate-universal.html",
    "hazards-glitches-logic.html": "hazards-in-combinational-circuits.html",
    "cmos-logic-gates.html": "cmos-logic-design-basics.html"
}

# 1. Update the files with meta refresh
for old_file, new_file in redirects.items():
    file_path = os.path.join(base_dir, old_file)
    if os.path.exists(file_path):
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=/blog/posts/{new_file}">
    <link rel="canonical" href="https://sqgate.online/blog/posts/{new_file}">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="/blog/posts/{new_file}">updated article</a>...</p>
</body>
</html>"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Redirected {old_file} -> {new_file}")

# 2. Remove the old files from blog/index.html
index_path = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

for old_file in redirects.keys():
    # Regex to find the <a href="..."> block for the old file
    # The block looks like:
    # <a href="/blog/posts/old_file" class="card">
    # ...
    # </a>
    pattern = rf'<a href="/blog/posts/{old_file}" class="card">.*?</a>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Cleaned up blog/index.html")
