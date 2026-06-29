import os
import re

def fix_bugs():
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.html'):
                filepath = os.path.join(root, name)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Remove favicon.svg
                content = re.sub(r'^\s*<link rel="icon" type="image/svg\+xml" href="/favicon\.svg" />\n?', '', content, flags=re.MULTILINE)
                
                # 2. Remove the modal HTML
                # First remove the comment if it exists
                content = re.sub(r'<!-- GLOBAL ERROR HANDLER -->\n?', '', content)
                # Then remove the style block and modal div
                modal_regex = r'<style>\s*#sqgate-error-modal\b.*?</style>\s*<div id="sqgate-error-modal">.*?</div>\s*</div>\s*</div>\n?'
                content = re.sub(modal_regex, '', content, flags=re.DOTALL)
                
                # 3. Remove showGlobalError function inside a script block
                script_func_regex = r'<script>\s*function showGlobalError.*?}\s*</script>\n?'
                content = re.sub(script_func_regex, '', content, flags=re.DOTALL)
                
                # Also remove it if it's just the function (without script tags)
                func_regex = r'function showGlobalError\([^\)]*\)\s*\{[^\}]+\}\s*'
                content = re.sub(func_regex, '', content, flags=re.DOTALL)
                
                # Clean up empty script tags left behind
                content = re.sub(r'<script>\s*</script>\n?', '', content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    fix_bugs()
