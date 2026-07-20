import re

with open(r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the placeholder article
placeholder_regex = r'<a href="/blog/posts/understanding-metastability-clock-domain-crossing\.html" class="card">.*?<h2 class="card-title">Metastability and Clock Domain Crossing \(CDC\) in Digital Design</h2>\s*<p class="card-desc">This is a placeholder article because no API key was provided\.\.\.\.</p>.*?</a>'
content = re.sub(placeholder_regex, '', content, flags=re.DOTALL)

# 2. Fix the duplicate block. We know there are 10 posts in the "Advanced Series".
# Let's find the first instance of 'The Evolution of Digital Logic: From Relays to Silicon'
# and see if it repeats.
# A simpler way is to find the exact block that is duplicated.
# Let's see if we can identify the duplicated block by looking for "<!-- Post 1 -->" to "<!-- Post 10 -->"
# If not, let's just use string finding.

evolution_idx = content.find('The Evolution of Digital Logic: From Relays to Silicon')
if evolution_idx != -1:
    second_idx = content.find('The Evolution of Digital Logic: From Relays to Silicon', evolution_idx + 1)
    if second_idx != -1:
        print("Found duplicate Evolution of Digital Logic.")
        # Find the start of the card
        card_start1 = content.rfind('<a href="/blog/posts/1-evolution-of-logic.html"', 0, evolution_idx)
        card_start2 = content.rfind('<a href="/blog/posts/1-evolution-of-logic.html"', 0, second_idx)
        
        # We need to remove the block starting from card_start2.
        # But where does it end? Probably before `<!-- Posts will be injected here by the build script -->`
        # Let's check what's before card_start2.
        print(f"Start 1: {card_start1}, Start 2: {card_start2}")
        
        # Assuming the duplicate block is exactly the same length.
        # Let's just find the injection marker.
        injection_marker = "<!-- Posts will be injected here by the build script -->"
        marker_idx = content.find(injection_marker)
        
        if card_start2 != -1 and marker_idx != -1 and card_start2 < marker_idx:
            print("Removing duplicate block...")
            # Remove from card_start2 to just before the marker
            content = content[:card_start2] + content[marker_idx:]

with open(r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done fixing blog/index.html")
