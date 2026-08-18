import re

def replace_seo_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open('new_seo_content.txt', 'r', encoding='windows-1252', errors='ignore') as f:
        new_content = f.read()

    pattern = r'<!-- SEO TOOL DESCRIPTIONS FOR ADSENSE CRAWLER -->\s*<div[^>]*>\s*<h3[^>]*>How Our Digital Logic Tools.*?</div>'
    
    new_html = re.sub(pattern, new_content, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

replace_seo_content('home/index.html')
replace_seo_content('index.html')
print("Replaced in home/index.html and index.html")
