import os
import re

competitors = ['logisim', 'tinkercad', 'circuitverse', 'falstad', 'logicly']

for comp in competitors:
    filepath = f"{comp}/index.html"
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove the redirect script
    html = re.sub(r'<script>\s*setTimeout.*?window\.location\.href.*?</script>', '', html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Redirects removed.")
