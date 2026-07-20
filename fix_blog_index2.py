with open(r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# The duplicate block is exactly from line 413 to 552 (0-indexed: 412 to 551).
# We should verify it starts with `<a href="/blog/posts/evolution-of-digital-logic.html"`
if 'evolution-of-digital-logic' in lines[412]:
    print("Found duplicate block at line 413. Deleting...")
    del lines[412:552]

# Now let's remove the placeholder
placeholder_start = -1
placeholder_end = -1

for i, line in enumerate(lines):
    if 'understanding-metastability-clock-domain-crossing.html' in line:
        # Check if it has the placeholder text inside it
        has_placeholder = False
        for j in range(i, min(i+15, len(lines))):
            if 'This is a placeholder article because no API key was provided' in lines[j]:
                has_placeholder = True
                break
        if has_placeholder:
            placeholder_start = i
            # Find the closing </a>
            for j in range(i, len(lines)):
                if '</a>' in lines[j]:
                    placeholder_end = j
                    break
            break

if placeholder_start != -1 and placeholder_end != -1:
    print(f"Removing placeholder block from {placeholder_start} to {placeholder_end}")
    del lines[placeholder_start:placeholder_end+1]

with open(r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
