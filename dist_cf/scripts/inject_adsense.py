import glob

target = 'ca-pub-7398330076279399'
script_tag = '\n  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7398330076279399" crossorigin="anonymous"></script>\n</head>'

for filepath in glob.glob('**/*.html', recursive=True):
    if 'dist_cf' in filepath or 'google1e701d9c9d06ac46.html' in filepath:
        continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if target not in content and '</head>' in content:
            new_content = content.replace('</head>', script_tag)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Injected AdSense into {filepath}')
    except Exception as e:
        pass
