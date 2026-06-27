import os

old_script = "<script>window.onerror=function(msg,u,l,c,e){var err=document.createElement('div');err.style.cssText='position:fixed;top:0;left:0;width:100%;background:red;color:white;z-index:999999;padding:10px;font-family:monospace';err.innerText='ERROR: '+msg+' at line '+l;document.body.appendChild(err);};</script>"

new_error_handler = """
<!-- GLOBAL ERROR HANDLER -->
<style>
#sqgate-error-modal { position: fixed; inset: 0; z-index: 999999; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px); font-family: 'Outfit', sans-serif; opacity: 0; pointer-events: none; transition: opacity 0.3s; }
#sqgate-error-modal.show { opacity: 1; pointer-events: auto; }
.sqgate-em-box { background: #1e293b; border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 32px; max-width: 420px; width: 90%; box-shadow: 0 24px 64px rgba(0,0,0,0.6); text-align: center; color: #e2e8f0; transform: translateY(20px); transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
#sqgate-error-modal.show .sqgate-em-box { transform: translateY(0); }
.sqgate-em-icon { font-size: 48px; color: #ef4444; margin-bottom: 16px; }
.sqgate-em-title { font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #fff; }
.sqgate-em-msg { font-size: 14px; color: #94a3b8; margin-bottom: 24px; line-height: 1.6; }
.sqgate-em-actions { display: flex; gap: 12px; justify-content: center; }
.sqgate-em-btn { padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.2s; border: none; text-decoration: none; display: inline-flex; align-items: center; justify-content: center;}
.sqgate-em-btn-primary { background: #7248b9; color: #fff; }
.sqgate-em-btn-primary:hover { background: #5b3a94; transform: translateY(-2px); }
.sqgate-em-btn-secondary { background: transparent; color: #cbd5e1; border: 1px solid rgba(255,255,255,0.2); }
.sqgate-em-btn-secondary:hover { background: rgba(255,255,255,0.05); color: #fff; }
</style>
<div id="sqgate-error-modal">
  <div class="sqgate-em-box">
    <div class="sqgate-em-icon">⚠️</div>
    <div class="sqgate-em-title">Oops! Something went wrong.</div>
    <div class="sqgate-em-msg">The application encountered an unexpected issue. You can report this to help us fix it!</div>
    <div class="sqgate-em-actions">
      <button class="sqgate-em-btn sqgate-em-btn-secondary" onclick="document.getElementById('sqgate-error-modal').classList.remove('show')">Dismiss</button>
      <a class="sqgate-em-btn sqgate-em-btn-primary" href="https://docs.google.com/forms/d/e/1FAIpQLSc5AzzP2NccDkCbKAb5mVvefYFc5_X-EkJZx5RLWO7aqQ_8cw/viewform" target="_blank">Report Problem</a>
    </div>
  </div>
</div>
<script>
function showGlobalError(msg) {
  var m = document.getElementById('sqgate-error-modal');
  if(m && !m.classList.contains('show')) m.classList.add('show');
}
window.addEventListener('error', function(e) { showGlobalError(e.message); });
window.addEventListener('unhandledrejection', function(e) { showGlobalError(e.reason); });
</script>
</body>
"""

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove old script
    if old_script in content:
        content = content.replace(old_script, '')
        
    # 2. Inject new handler before </body>
    if '<!-- GLOBAL ERROR HANDLER -->' not in content and '</body>' in content:
        content = content.replace('</body>', new_error_handler)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Patched {filepath}")

for root, _, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            patch_file(os.path.join(root, file))
