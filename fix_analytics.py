import os
import glob
import re

blog_posts_path = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\posts\*.html"
real_ga = "G-72EG9VJELZ"
real_adsense = "ca-pub-7398330076279399"

# Dummy GA variants found:
ga_patterns = [
    "G-XXXXXXXXXX",
    "G-SQGATE1234",
    "G-SQGATE123",
    "G-1234567890",
    "G-SQGATETRACK",
    "G-SQGATEBLOG",
    "G-SQGATEXXXX",
    "G-YOUR_MEASUREMENT_ID"
]

# Dummy AdSense variants:
adsense_patterns = [
    "ca-pub-XXXXXXXXXXXXXXXX"
]

files = glob.glob(blog_posts_path)
count = 0

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Replace GA
    for pattern in ga_patterns:
        if pattern in content:
            content = content.replace(pattern, real_ga)
            modified = True
            
    # Replace AdSense
    for pattern in adsense_patterns:
        if pattern in content:
            content = content.replace(pattern, real_adsense)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed analytics and adsense IDs in {count} blog posts.")
