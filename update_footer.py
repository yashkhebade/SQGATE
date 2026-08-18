import re

def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update login screen footer
    login_footer = r'<a href="/terms" style="color:rgba\(255,255,255,0\.6\);text-decoration:none;">Terms of Service</a> &bull;\s*<a href="/privacy" style="color:rgba\(255,255,255,0\.6\);text-decoration:none;">Privacy Policy</a>'
    new_login_footer = '<a href="/about.html" style="color:rgba(255,255,255,0.6);text-decoration:none;">About Us</a> &bull; <a href="/terms" style="color:rgba(255,255,255,0.6);text-decoration:none;">Terms of Service</a> &bull; <a href="/privacy" style="color:rgba(255,255,255,0.6);text-decoration:none;">Privacy Policy</a>'
    content = re.sub(login_footer, new_login_footer, content, flags=re.DOTALL)

    # 2. Update dashboard footer
    dash_footer = r'<a href="/terms" style="color:var\(--t2\);text-decoration:none;">Terms</a> &nbsp;\|&nbsp;\s*<a href="/privacy" style="color:var\(--t2\);text-decoration:none;">Privacy</a> &nbsp;\|&nbsp;\s*<a href="/refund" style="color:var\(--t2\);text-decoration:none;">Refund Policy</a> &nbsp;\|&nbsp;\s*<a href="/contact.html" style="color:var\(--t2\);text-decoration:none;">Contact Us</a>'
    
    new_dash_footer = '<a href="/about.html" style="color:var(--t2);text-decoration:none;">About</a> &nbsp;|&nbsp; <a href="/terms" style="color:var(--t2);text-decoration:none;">Terms</a> &nbsp;|&nbsp; <a href="/privacy" style="color:var(--t2);text-decoration:none;">Privacy</a> &nbsp;|&nbsp; <a href="/refund" style="color:var(--t2);text-decoration:none;">Refund Policy</a> &nbsp;|&nbsp; <a href="/contact.html" style="color:var(--t2);text-decoration:none;">Contact Us</a>'
    content = re.sub(dash_footer, new_dash_footer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_footer('home/index.html')
update_footer('index.html')
