import glob
import os
import re

files = glob.glob('**/*.html', recursive=True)
files = [f for f in files if 'node_modules' not in f and 'dist_cf' not in f]

print('| Page | Word Count | Canvas Element? | Notes |')
print('|------|------------|-----------------|-------|')
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        try:
            with open(f, 'r', encoding='utf-16') as file:
                content = file.read()
        except UnicodeDecodeError:
            with open(f, 'r', errors='ignore') as file:
                content = file.read()
        
    # Remove script and style tags using regex
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?</style>', '', content, flags=re.DOTALL)
    
    # Extract text using regex
    text = re.sub(r'<[^>]+>', ' ', content)
    
    # Clean up text and count words
    words = re.findall(r'\w+', text)
    word_count = len(words)
    
    has_canvas = 'Yes' if '<canvas' in content else 'No'
    
    print(f'| {f} | {word_count} | {has_canvas} | |')
