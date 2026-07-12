import os
import re

workspace_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"

def fix_canonicals():
    count = 0
    for root, dirs, files in os.walk(workspace_dir):
        if ".git" in root or "node_modules" in root or ".wrangler" in root or "dist_cf" in root:
            continue
        
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                # Determine the correct canonical URL
                rel_path = os.path.relpath(filepath, workspace_dir).replace('\\', '/')
                
                if rel_path == "index.html" or rel_path == "home/index.html":
                    correct_url = "https://sqgate.online/"
                elif rel_path.endswith("/index.html"):
                    # e.g. logigator/index.html -> https://sqgate.online/logigator/
                    folder_path = rel_path[:-10] # remove index.html
                    correct_url = f"https://sqgate.online/{folder_path}"
                else:
                    # e.g. pricing.html -> https://sqgate.online/pricing
                    name_without_ext = rel_path[:-5]
                    correct_url = f"https://sqgate.online/{name_without_ext}"
                
                # Read the file
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
                
                # Replace the canonical tag
                # Regex to match <link rel="canonical" href="...">
                pattern = r'<link\s+rel=["\']canonical["\']\s+href=["\'](https://sqgate\.online/?[^"\']*)["\']\s*/?>'
                
                def replacer(match):
                    old_url = match.group(1)
                    if old_url != correct_url:
                        print(f"Updating {rel_path}: {old_url} -> {correct_url}")
                    return f'<link rel="canonical" href="{correct_url}">'
                
                new_content = re.sub(pattern, replacer, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
    
    print(f"Fixed canonical tags in {count} files.")

if __name__ == "__main__":
    fix_canonicals()
