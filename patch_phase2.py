import os

def patch_fsm():
    filepath = 'fsm/index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    css_injection = """
/* ── MOBILE UI REDESIGN ── */
.mobile-only { display: none !important; }
@media (max-width: 768px) {
  .mobile-only { display: inline-flex !important; }
  
  #fsm-panel {
    position: absolute;
    top: 0; bottom: 0; right: 0;
    z-index: 1000;
    width: 280px !important;
    transform: translateX(100%);
    transition: transform 0.3s cubic-bezier(0.2,0.8,0.2,1);
    box-shadow: -4px 0 40px rgba(0,0,0,0.8);
  }
  #fsm-panel.mobile-open {
    transform: translateX(0);
  }

  .tb-btn, .panel-tab {
    min-height: 44px;
    min-width: 44px;
  }
  
  #fsm-toolbar {
    overflow-x: auto;
    padding-right: 16px;
  }
  #fsm-toolbar::-webkit-scrollbar { display: none; }
  
  /* Make sure app container handles relative positioning for absolute panel */
  #fsm-app { position: relative; overflow: hidden; }
}
</style>
"""
    if '/* ── MOBILE UI REDESIGN ── */' not in content:
        content = content.replace('</style>', css_injection, 1)
        
        # Inject toggle button in fsm-toolbar
        btn_html = """
    <div class="tb-group mobile-only" style="margin-left:8px; border-right:none; border-left:1px solid var(--border);">
      <button class="tb-btn mobile-only" onclick="document.getElementById('fsm-panel').classList.toggle('mobile-open')" style="background:var(--bg-accent); color:var(--text-accent);"><i class="ti ti-layout-sidebar-right"></i> Props</button>
    </div>
  </div>"""
        content = content.replace('</div>\n  <!-- TOOLBAR (canvas) END -->', btn_html, 1) # Note: we just replace the end of fsm-toolbar if there is a comment.
        # Wait, the end of fsm-toolbar is just </div>.
        
        # safer injection point: after the "Encoding" select group
        enc_group = """      </select>
    </div>"""
        
        new_enc_group = enc_group + """
    <div class="tb-group mobile-only" style="border-right:none; border-left:1px solid var(--border); padding-left:8px;">
      <button class="tb-btn" onclick="document.getElementById('fsm-panel').classList.toggle('mobile-open')" style="width:auto; padding:0 12px; gap:6px; background:rgba(139,92,246,0.15); color:#8b5cf6;"><i class="ti ti-layout-sidebar-right"></i> Props</button>
    </div>"""
        content = content.replace(enc_group, new_enc_group, 1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Patched fsm/index.html")

def patch_kmap():
    filepath = 'k-map/index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    css_injection = """
/* ── MOBILE UI REDESIGN ── */
@media (max-width: 768px) {
  .vbtn, .rstbtn {
    min-height: 44px;
    padding: 0 16px;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .km-ctrl-row {
    padding: 12px;
    gap: 12px;
  }
}
</style>
"""
    if '/* ── MOBILE UI REDESIGN ── */' not in content:
        content = content.replace('</style>', css_injection, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Patched k-map/index.html")

patch_fsm()
patch_kmap()
