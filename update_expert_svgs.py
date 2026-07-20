import os
import re

filepath = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS for Expert vs Beginner SVGs
css_to_add = """
.svg-expert { display: none; }
.split-features-container.expert-mode .svg-beginner { display: none; }
.split-features-container.expert-mode .svg-expert { display: block; }
"""
if '.svg-expert {' not in content:
    content = content.replace('/* SPLIT LAYOUT STYLES */', '/* SPLIT LAYOUT STYLES */\n' + css_to_add)

# Find JS block and add expert-mode class toggling
if "document.getElementById('split-features').classList.add('expert-mode');" not in content:
    js_target = "lblExpert.classList.add('active');"
    js_replace = "lblExpert.classList.add('active');\n        document.getElementById('split-features').classList.add('expert-mode');"
    content = content.replace(js_target, js_replace)

    js_target_2 = "lblBeginner.classList.add('active');"
    js_replace_2 = "lblBeginner.classList.add('active');\n        document.getElementById('split-features').classList.remove('expert-mode');"
    content = content.replace(js_target_2, js_replace_2)

# SIMULATOR REPLACEMENT
sim_expert_svg = """
            <svg class="svg-expert" width="300" height="200" viewBox="0 0 300 200">
              <!-- Inputs -->
              <text x="30" y="65" fill="#94a3b8" font-family="monospace" font-size="12">A[7:0]</text>
              <text x="30" y="115" fill="#94a3b8" font-family="monospace" font-size="12">B[7:0]</text>
              <!-- Buses -->
              <path d="M 75 60 L 120 70" stroke="#334155" stroke-width="4" fill="none"/>
              <path class="anim-wire" d="M 75 60 L 120 70" stroke="#22d3ee" stroke-width="4" fill="none"/>
              <path d="M 85 55 L 95 75" stroke="#334155" stroke-width="2"/>
              <path d="M 75 110 L 120 100" stroke="#334155" stroke-width="4" fill="none"/>
              <path class="anim-wire" d="M 75 110 L 120 100" stroke="#22d3ee" stroke-width="4" fill="none"/>
              <path d="M 85 95 L 95 115" stroke="#334155" stroke-width="2"/>
              <!-- ALU Block -->
              <path d="M 120 40 L 160 40 L 180 60 L 180 110 L 160 130 L 120 130 L 120 95 L 130 85 L 120 75 Z" fill="rgba(34,211,238,0.05)" stroke="#22d3ee" stroke-width="2"/>
              <text x="145" y="90" fill="#22d3ee" font-family="monospace" font-size="14" font-weight="bold">ALU</text>
              <!-- Opcode control -->
              <path d="M 150 150 L 150 120" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2 2" fill="none"/>
              <text x="150" y="165" fill="#f59e0b" font-family="monospace" font-size="10" text-anchor="middle">OP=ADD</text>
              <!-- Output Bus -->
              <path d="M 180 85 L 240 85" stroke="#334155" stroke-width="4" fill="none"/>
              <path class="anim-wire" d="M 180 85 L 240 85" stroke="#22d3ee" stroke-width="4" fill="none"/>
              <path d="M 205 75 L 215 95" stroke="#334155" stroke-width="2"/>
              <text x="260" y="90" fill="#94a3b8" font-family="monospace" font-size="12">Y[7:0]</text>
            </svg>
"""
sim_regex = r'(<div class="preview-animation active" id="anim-sim">)(\s*<svg.*?<\/svg>)'
content = re.sub(sim_regex, lambda m: f'{m.group(1)}\n<div class="svg-beginner">{m.group(2)}</div>\n{sim_expert_svg}', content, flags=re.DOTALL)

# FSM REPLACEMENT
fsm_expert_svg = """
            <svg class="svg-expert" width="300" height="200" viewBox="0 0 300 200">
              <circle cx="80" cy="100" r="28" fill="rgba(33, 41, 59, 0.8)" stroke="#64748b" stroke-width="2"/>
              <text x="80" y="98" fill="#fff" font-family="monospace" font-size="10" text-anchor="middle">WAIT</text>
              <text x="80" y="112" fill="#94a3b8" font-family="monospace" font-size="9" text-anchor="middle">2'b00</text>
              
              <circle cx="220" cy="100" r="28" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="2" class="anim-node"/>
              <text x="220" y="98" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">GRANT</text>
              <text x="220" y="112" fill="#10b981" font-family="monospace" font-size="9" text-anchor="middle">2'b01</text>

              <path d="M 100 80 Q 150 50 195 75" fill="none" stroke="#10b981" stroke-width="2" class="anim-arrow"/>
              <polygon points="190,70 200,78 185,82" fill="#10b981" style="stroke:none;" transform="rotate(-10 195 75)"/>
              <text x="150" y="45" fill="#10b981" font-family="monospace" font-size="9" text-anchor="middle">req &amp; ~busy / gnt=1</text>
              
              <path d="M 200 120 Q 150 150 105 125" fill="none" stroke="#64748b" stroke-width="2"/>
              <polygon points="110,130 100,122 115,118" fill="#64748b" style="stroke:none;" transform="rotate(-10 105 125)"/>
              <text x="150" y="165" fill="#64748b" font-family="monospace" font-size="9" text-anchor="middle">busy=0 / gnt=0</text>
              
              <path d="M 60 78 C 30 40 30 160 60 122" fill="none" stroke="#64748b" stroke-width="2"/>
              <text x="35" y="104" fill="#64748b" font-family="monospace" font-size="9" text-anchor="end">~req</text>
            </svg>
"""
fsm_regex = r'(<div class="preview-animation" id="anim-fsm">)(\s*<svg.*?<\/svg>)'
content = re.sub(fsm_regex, lambda m: f'{m.group(1)}\n<div class="svg-beginner">{m.group(2)}</div>\n{fsm_expert_svg}', content, flags=re.DOTALL)

# QUEST REPLACEMENT
quest_expert_svg = """
            <svg class="svg-expert" width="300" height="200" viewBox="0 0 300 200">
              <text x="30" y="50" fill="#94a3b8" font-family="monospace" font-size="10">CLK</text>
              <path d="M 60 50 L 75 50 L 75 30 L 105 30 L 105 50 L 135 50 L 135 30 L 165 30 L 165 50 L 195 50" stroke="#334155" stroke-width="2" fill="none"/>
              
              <text x="30" y="90" fill="#94a3b8" font-family="monospace" font-size="10">D_IN</text>
              <path d="M 60 90 L 90 90 L 90 70 L 150 70 L 150 90 L 195 90" stroke="#f59e0b" stroke-width="2" fill="none"/>
              
              <text x="30" y="130" fill="#94a3b8" font-family="monospace" font-size="10">Q_OUT</text>
              <path d="M 60 130 L 105 130 L 105 110 L 165 110 L 165 130 L 195 130" stroke="#64748b" stroke-width="2" stroke-dasharray="4 4" fill="none"/>

              <g class="anim-puzzle-piece" transform="translate(100, -10)">
                <rect x="150" y="110" width="40" height="30" rx="4" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
                <path d="M 150 120 L 155 125 L 150 130" stroke="#10b981" stroke-width="1" fill="none"/>
                <text x="175" y="129" fill="#10b981" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">D-FF</text>
              </g>
              
              <line x1="105" y1="20" x2="105" y2="140" stroke="#ef4444" stroke-width="1" stroke-dasharray="2 2" opacity="0.5"/>
              <text x="110" y="145" fill="#ef4444" font-family="monospace" font-size="8">T_su</text>
            </svg>
"""
quest_regex = r'(<div class="preview-animation" id="anim-quest">)(\s*<svg.*?<\/svg>)'
content = re.sub(quest_regex, lambda m: f'{m.group(1)}\n<div class="svg-beginner">{m.group(2)}</div>\n{quest_expert_svg}', content, flags=re.DOTALL)

# KMAP REPLACEMENT
kmap_expert_svg = """
            <svg class="svg-expert" width="300" height="200" viewBox="0 0 300 200">
              <g transform="translate(60, 30)">
                <line x1="0" y1="0" x2="-30" y2="-30" stroke="#64748b" stroke-width="1"/>
                <text x="-25" y="-5" fill="#94a3b8" font-family="monospace" font-size="10">AB</text>
                <text x="-5" y="-20" fill="#94a3b8" font-family="monospace" font-size="10">CD</text>
                
                <text x="20" y="-10" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">00</text>
                <text x="60" y="-10" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">01</text>
                <text x="100" y="-10" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">11</text>
                <text x="140" y="-10" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">10</text>
                
                <text x="-15" y="25" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="end">00</text>
                <text x="-15" y="65" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="end">01</text>
                <text x="-15" y="105" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="end">11</text>
                <text x="-15" y="145" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="end">10</text>
                
                <path d="M 0 0 h 160 v 160 h -160 Z" fill="none" stroke="#334155" stroke-width="1"/>
                <path d="M 40 0 v 160 M 80 0 v 160 M 120 0 v 160 M 0 40 h 160 M 0 80 h 160 M 0 120 h 160" stroke="#334155" stroke-width="1" fill="none"/>
                
                <text x="20" y="25" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>
                <text x="60" y="25" fill="#f59e0b" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <text x="100" y="25" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>
                <text x="140" y="25" fill="#f59e0b" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                
                <text x="20" y="65" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>
                <text x="60" y="65" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>
                <text x="100" y="65" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>
                <text x="140" y="65" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>

                <text x="20" y="105" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>
                <text x="60" y="105" fill="#f59e0b" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <text x="100" y="105" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>
                <text x="140" y="105" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>

                <text x="20" y="145" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>
                <text x="60" y="145" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">0</text>
                <text x="100" y="145" fill="#f59e0b" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">X</text>
                <text x="140" y="145" fill="#fff" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">1</text>

                <rect x="45" y="5" width="70" height="70" class="anim-kmap-group"/>
                <rect x="85" y="85" width="70" height="70" class="anim-kmap-group" style="stroke:#22d3ee; fill:rgba(34,211,238,0.2); animation-delay: 1.5s;"/>
                <rect x="85" y="5" width="30" height="150" class="anim-kmap-group" style="stroke:#f59e0b; fill:rgba(245,158,11,0.2); animation-delay: 0.75s;"/>
              </g>
            </svg>
"""
kmap_regex = r'(<div class="preview-animation" id="anim-kmap">)(\s*<svg.*?<\/svg>)'
content = re.sub(kmap_regex, lambda m: f'{m.group(1)}\n<div class="svg-beginner">{m.group(2)}</div>\n{kmap_expert_svg}', content, flags=re.DOTALL)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Added expert SVGs successfully.")
