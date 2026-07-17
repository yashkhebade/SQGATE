import glob

files = glob.glob(r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\posts\*.html")
tag = '<meta name="google-adsense-account" content="ca-pub-7398330076279399">\n'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "google-adsense-account" not in content:
        content = content.replace('<!-- Google AdSense -->', f'<!-- Google AdSense -->\n    {tag}')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
print(f"Injected into {len(files)} files.")
