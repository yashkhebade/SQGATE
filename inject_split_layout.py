import os

filepath = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '    <!-- DIGITAL DESIGN SUITE -->'
end_marker = '    <!-- SEO TOOL DESCRIPTIONS FOR ADSENSE CRAWLER -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

html_code = """    <!-- DIGITAL DESIGN SUITE -->
    <style>
/* SPLIT LAYOUT STYLES */
.split-features-container {
  max-width: 1200px;
  margin: 0 auto 80px auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s var(--ease), transform 0.8s var(--ease);
}
.split-features-container.visible {
  opacity: 1;
  transform: translateY(0);
}

@media(max-width: 900px) {
  .split-features-container {
    grid-template-columns: 1fr;
  }
}

/* LEFT COLUMN - NAVIGATION */
.features-nav {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.feature-nav-item {
  padding: 24px;
  border-radius: 16px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.3s var(--ease);
  position: relative;
  overflow: hidden;
  text-decoration: none;
  display: block;
}

.feature-nav-item.active {
  background: rgba(255, 255, 255, 0.03);
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 0 20px rgba(139, 92, 246, 0.1);
}

.feature-nav-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 4px;
  background: var(--acc);
  transform: scaleY(0);
  transition: transform 0.3s var(--ease);
  transform-origin: center;
}

.feature-nav-item.active::before {
  transform: scaleY(1);
}

.feature-nav-item.tc-cyan.active::before { background: var(--hi); }
.feature-nav-item.tc-emerald.active::before { background: var(--acb); }
.feature-nav-item.tc-amber.active::before { background: var(--aca); }
.feature-nav-item.tc-coral.active::before { background: #f87171; } 

.feature-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: var(--fsans);
  font-weight: 600;
  font-size: 20px;
  color: var(--t1);
  margin-bottom: 8px;
}

.feature-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: rgba(255,255,255,0.05);
}

.feature-desc {
  font-size: 15px;
  color: var(--t2);
  line-height: 1.6;
}

/* TOGGLE SWITCH */
.copy-toggle-container {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 12px;
  margin-bottom: 32px;
  padding: 0 10px;
}

.copy-toggle-label {
  font-size: 14px;
  font-weight: 500;
  color: var(--t2);
  transition: color 0.3s;
}
.copy-toggle-label.active {
  color: var(--t1);
}

.copy-toggle {
  position: relative;
  width: 52px;
  height: 28px;
  background: rgba(255,255,255,0.1);
  border-radius: 14px;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,0.1);
  transition: background 0.3s;
}

.copy-toggle::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 22px;
  height: 22px;
  background: var(--acc);
  border-radius: 50%;
  transition: transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);
  box-shadow: 0 0 10px var(--acc-glow);
}

.copy-toggle.expert::after {
  transform: translateX(24px);
  background: var(--hi);
  box-shadow: 0 0 10px var(--hi-glow);
}

/* RIGHT COLUMN - PREVIEW WINDOW */
.preview-window {
  background: rgba(12, 15, 28, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  position: sticky;
  top: 100px;
  height: 500px;
}

.preview-header {
  height: 40px;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 8px;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.preview-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}
.preview-dot.r { background: #ef4444; }
.preview-dot.y { background: #f59e0b; }
.preview-dot.g { background: #10b981; }

.preview-stage {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: radial-gradient(circle at center, rgba(34, 42, 69, 0.4) 0%, rgba(6, 8, 19, 0.8) 100%);
}

.preview-animation {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.5s var(--ease), transform 0.5s var(--ease);
  transform: scale(0.95);
}

.preview-animation.active {
  opacity: 1;
  pointer-events: auto;
  transform: scale(1);
}

/* Launch Button Overlay */
.preview-launch {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.2);
  padding: 10px 24px;
  border-radius: 20px;
  color: #fff;
  font-family: var(--fsans);
  font-weight: 500;
  font-size: 14px;
  text-decoration: none;
  backdrop-filter: blur(10px);
  transition: all 0.3s;
  opacity: 0;
  transform: translate(-50%, 10px);
}

.preview-window:hover .preview-launch {
  opacity: 1;
  transform: translate(-50%, 0);
}
.preview-launch:hover {
  background: var(--acc);
  border-color: var(--acc);
  box-shadow: 0 0 20px var(--acc-glow);
}

/* SVG ANIMATION STYLES */
.anim-wire { stroke-dasharray: 200; stroke-dashoffset: 200; animation: wireDraw 3s infinite; }
@keyframes wireDraw {
  0% { stroke-dashoffset: 200; }
  30% { stroke-dashoffset: 0; }
  100% { stroke-dashoffset: 0; }
}
.anim-bulb { fill: rgba(255,255,255,0.1); stroke: #cbd5e1; transition: all 0.3s; animation: bulbGlow 3s infinite; }
@keyframes bulbGlow {
  0%, 25% { fill: rgba(255,255,255,0.1); filter: none; }
  30%, 90% { fill: #f59e0b; filter: drop-shadow(0 0 10px #f59e0b); }
  100% { fill: rgba(255,255,255,0.1); filter: none; }
}
.anim-signal { fill: #22d3ee; filter: drop-shadow(0 0 5px #22d3ee); opacity: 0; animation: signalMove 3s infinite; }
@keyframes signalMove {
  0%, 5% { opacity: 0; transform: translateX(0); }
  10% { opacity: 1; transform: translateX(0); }
  25% { opacity: 1; transform: translateX(100px); }
  30%, 100% { opacity: 0; transform: translateX(100px); }
}

.anim-node { fill: rgba(16, 185, 129, 0.1); stroke: #10b981; stroke-width: 2; animation: nodePulse 4s infinite; }
.anim-node-2 { animation-delay: 1s; }
.anim-node-3 { animation-delay: 2s; }
@keyframes nodePulse {
  0%, 100% { fill: rgba(16, 185, 129, 0.1); box-shadow: none; }
  10%, 30% { fill: rgba(16, 185, 129, 0.4); filter: drop-shadow(0 0 15px #10b981); }
  40% { fill: rgba(16, 185, 129, 0.1); box-shadow: none; }
}
.anim-arrow { stroke: #64748b; stroke-width: 2; stroke-dasharray: 100; stroke-dashoffset: 100; animation: arrowDraw 4s infinite; }
.anim-arrow-2 { animation-delay: 1s; }
@keyframes arrowDraw {
  0%, 10% { stroke-dashoffset: 100; stroke: #64748b;}
  20%, 40% { stroke-dashoffset: 0; stroke: #10b981; }
  50%, 100% { stroke-dashoffset: 0; stroke: #64748b; }
}

.anim-puzzle-piece { transform: translate(0, 50px); opacity: 0; animation: pieceSnap 3s infinite; }
@keyframes pieceSnap {
  0% { transform: translate(0, 50px) scale(0.9); opacity: 0; }
  15% { transform: translate(0, 0) scale(1.05); opacity: 1; }
  25%, 80% { transform: translate(0, 0) scale(1); opacity: 1; filter: drop-shadow(0 0 10px #f59e0b); }
  90%, 100% { opacity: 0; }
}
.anim-puzzle-target { stroke-dasharray: 4 4; stroke: #64748b; animation: targetGlow 3s infinite; }
@keyframes targetGlow {
  0%, 20% { stroke: #64748b; fill: none; }
  25%, 80% { stroke: #f59e0b; fill: rgba(245, 158, 11, 0.1); stroke-dasharray: none; }
  90%, 100% { stroke: #64748b; fill: none; }
}

.anim-kmap-cell { fill: transparent; stroke: #334155; }
.anim-kmap-group { fill: rgba(248, 113, 113, 0.2); stroke: #f87171; stroke-width: 2; rx: 4; opacity: 0; animation: kmapGroup 3s infinite; }
@keyframes kmapGroup {
  0%, 20% { opacity: 0; transform: scale(0.9); transform-origin: center; }
  30%, 80% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 8px #f87171); }
  90%, 100% { opacity: 0; }
}
    </style>

    <div id="features" class="proj-section-title">THE DIGITAL DESIGN SUITE</div>
    <div class="split-features-container" id="split-features">
      
      <!-- LEFT COLUMN -->
      <div class="features-nav">
        
        <!-- TOGGLE SWITCH -->
        <div class="copy-toggle-container">
          <span class="copy-toggle-label active" id="lbl-beginner">Beginner</span>
          <div class="copy-toggle" id="copy-toggle-btn"></div>
          <span class="copy-toggle-label" id="lbl-expert">Expert</span>
        </div>

        <!-- ITEM 1 -->
        <a href="javascript:createNewProject()" class="feature-nav-item tc-cyan active" data-target="anim-sim">
          <div class="feature-title">
            <div class="feature-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line><line x1="12" y1="8" x2="12" y2="16"></line></svg></div>
            Visual Circuit Simulator
          </div>
          <div class="feature-desc desc-beginner">Build digital circuits like LEGO bricks. Drag and drop components, connect wires, and watch electricity flow instantly. No coding required.</div>
          <div class="feature-desc desc-expert" style="display:none;">Interactive gate-level simulation environment. Supports hierarchical design, bus routing, and real-time combinatorial logic validation.</div>
        </a>
        
        <!-- ITEM 2 -->
        <a href="/fsm" class="feature-nav-item tc-emerald" data-target="anim-fsm">
          <div class="feature-title">
            <div class="feature-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="12" r="3"></circle><path d="M9 12h6"></path><path d="M16 10l2 2-2 2"></path></svg></div>
            FSM Designer & Generator
          </div>
          <div class="feature-desc desc-beginner">Draw state machine diagrams on a canvas and let SQGate automatically write the complex code for you. Perfect for assignments.</div>
          <div class="feature-desc desc-expert" style="display:none;">Graphical Moore/Mealy machine entry tool with automated synthesizable Verilog HDL generation and testbench scaffolding.</div>
        </a>

        <!-- ITEM 3 -->
        <a href="/puzzle" class="feature-nav-item tc-amber" data-target="anim-quest">
          <div class="feature-title">
            <div class="feature-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg></div>
            Logic Quest (Puzzle Game)
          </div>
          <div class="feature-desc desc-beginner">Learn digital logic through play. Solve challenging puzzles by connecting the right gates to unlock the next level.</div>
          <div class="feature-desc desc-expert" style="display:none;">Gamified Boolean optimization challenges. Synthesize truth tables using restricted gate inventories to enforce logic minimization principles.</div>
        </a>

        <!-- ITEM 4 -->
        <a href="/k-map" class="feature-nav-item tc-coral" data-target="anim-kmap">
          <div class="feature-title">
            <div class="feature-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg></div>
            Interactive K-Map Solver
          </div>
          <div class="feature-desc desc-beginner">Stop struggling with messy math. Just click the cells in the grid, and we'll instantly give you the simplest equation.</div>
          <div class="feature-desc desc-expert" style="display:none;">Algorithmic Quine-McCluskey minimization for up to 6 variables. Instantly derives prime implicants and the simplified Sum of Products (SOP).</div>
        </a>

      </div>

      <!-- RIGHT COLUMN -->
      <div class="preview-window">
        <div class="preview-header">
          <div class="preview-dot r"></div>
          <div class="preview-dot y"></div>
          <div class="preview-dot g"></div>
        </div>
        
        <div class="preview-stage">
          
          <!-- SIMULATOR ANIMATION -->
          <div class="preview-animation active" id="anim-sim">
            <svg width="300" height="200" viewBox="0 0 300 200">
              <rect x="50" y="50" width="60" height="40" rx="4" fill="rgba(34,211,238,0.1)" stroke="#22d3ee" stroke-width="2"/>
              <text x="80" y="75" fill="#22d3ee" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">AND</text>
              
              <path d="M 110 70 L 210 70" stroke="#334155" stroke-width="4" fill="none"/>
              <path class="anim-wire" d="M 110 70 L 210 70" stroke="#22d3ee" stroke-width="4" fill="none"/>
              
              <circle class="anim-signal" cx="110" cy="70" r="4"/>
              
              <g transform="translate(210, 50)">
                <path class="anim-bulb" d="M15 40h10M20 40v-5m0 0a10 10 0 1 0-10-10 10 10 0 0 0 10 10z" stroke-width="2" stroke-linecap="round"/>
              </g>
            </svg>
            <a href="javascript:createNewProject()" class="preview-launch" id="launch-btn-sim">Launch Simulator</a>
          </div>

          <!-- FSM ANIMATION -->
          <div class="preview-animation" id="anim-fsm">
            <svg width="300" height="200" viewBox="0 0 300 200">
              <path d="M 100 100 Q 150 50 200 100" fill="none" stroke="#334155" stroke-width="2"/>
              <path class="anim-arrow" d="M 100 100 Q 150 50 200 100" fill="none" stroke-width="2"/>
              <polygon points="195,95 205,100 195,105" fill="#10b981" class="anim-arrow" style="stroke:none;"/>
              
              <path d="M 200 100 Q 150 150 100 100" fill="none" stroke="#334155" stroke-width="2"/>
              <path class="anim-arrow anim-arrow-2" d="M 200 100 Q 150 150 100 100" fill="none" stroke-width="2"/>
              <polygon points="105,105 95,100 105,95" fill="#10b981" class="anim-arrow anim-arrow-2" style="stroke:none;"/>

              <circle cx="100" cy="100" r="30" class="anim-node"/>
              <text x="100" y="105" fill="#fff" font-family="monospace" font-size="14" text-anchor="middle">S0</text>
              
              <circle cx="200" cy="100" r="30" class="anim-node anim-node-2"/>
              <text x="200" y="105" fill="#fff" font-family="monospace" font-size="14" text-anchor="middle">S1</text>
            </svg>
            <a href="/fsm" class="preview-launch" id="launch-btn-fsm">Launch FSM Designer</a>
          </div>

          <!-- QUEST ANIMATION -->
          <div class="preview-animation" id="anim-quest">
            <svg width="300" height="200" viewBox="0 0 300 200">
              <rect x="50" y="80" width="60" height="40" rx="4" fill="rgba(245,158,11,0.1)" stroke="#f59e0b" stroke-width="2"/>
              <text x="80" y="105" fill="#f59e0b" font-family="monospace" font-size="14" text-anchor="middle">XOR</text>
              
              <rect x="150" y="80" width="60" height="40" rx="4" class="anim-puzzle-target"/>
              <text x="180" y="105" fill="#64748b" font-family="monospace" font-size="12" text-anchor="middle">DROP</text>

              <g class="anim-puzzle-piece">
                <rect x="150" y="80" width="60" height="40" rx="4" fill="rgba(245,158,11,0.9)" stroke="#f59e0b" stroke-width="2"/>
                <text x="180" y="105" fill="#fff" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">AND</text>
              </g>
            </svg>
            <a href="/puzzle" class="preview-launch" id="launch-btn-quest">Play Logic Quest</a>
          </div>

          <!-- KMAP ANIMATION -->
          <div class="preview-animation" id="anim-kmap">
            <svg width="300" height="200" viewBox="0 0 300 200">
              <g transform="translate(70, 40)">
                <rect x="0" y="0" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="40" y="0" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="80" y="0" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="120" y="0" width="40" height="40" class="anim-kmap-cell"/>
                
                <rect x="0" y="40" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="40" y="40" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="80" y="40" width="40" height="40" class="anim-kmap-cell"/>
                <rect x="120" y="40" width="40" height="40" class="anim-kmap-cell"/>
                
                <text x="20" y="25" fill="#94a3b8" font-family="monospace" text-anchor="middle">0</text>
                <text x="60" y="25" fill="#fff" font-family="monospace" font-weight="bold" text-anchor="middle">1</text>
                <text x="100" y="25" fill="#fff" font-family="monospace" font-weight="bold" text-anchor="middle">1</text>
                <text x="140" y="25" fill="#94a3b8" font-family="monospace" text-anchor="middle">0</text>
                
                <text x="20" y="65" fill="#94a3b8" font-family="monospace" text-anchor="middle">0</text>
                <text x="60" y="65" fill="#fff" font-family="monospace" font-weight="bold" text-anchor="middle">1</text>
                <text x="100" y="65" fill="#fff" font-family="monospace" font-weight="bold" text-anchor="middle">1</text>
                <text x="140" y="65" fill="#94a3b8" font-family="monospace" text-anchor="middle">0</text>

                <rect x="35" y="5" width="90" height="70" class="anim-kmap-group"/>
              </g>
            </svg>
            <a href="/k-map" class="preview-launch" id="launch-btn-kmap">Launch K-Map Solver</a>
          </div>

        </div>
      </div>

    </div>
"""

js_code = """
<script>
document.addEventListener('DOMContentLoaded', () => {
  // Toggle logic
  const copyToggleBtn = document.getElementById('copy-toggle-btn');
  const lblBeginner = document.getElementById('lbl-beginner');
  const lblExpert = document.getElementById('lbl-expert');
  const descBeginners = document.querySelectorAll('.desc-beginner');
  const descExperts = document.querySelectorAll('.desc-expert');

  if(copyToggleBtn) {
    copyToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      e.preventDefault();
      const isExpert = copyToggleBtn.classList.toggle('expert');
      if(isExpert) {
        lblBeginner.classList.remove('active');
        lblExpert.classList.add('active');
        descBeginners.forEach(el => el.style.display = 'none');
        descExperts.forEach(el => el.style.display = 'block');
      } else {
        lblExpert.classList.remove('active');
        lblBeginner.classList.add('active');
        descExperts.forEach(el => el.style.display = 'none');
        descBeginners.forEach(el => el.style.display = 'block');
      }
    });
  }

  // Nav item active state
  const navItems = document.querySelectorAll('.feature-nav-item');
  const animations = document.querySelectorAll('.preview-animation');

  navItems.forEach(item => {
    item.addEventListener('mouseenter', () => activateItem(item));
    item.addEventListener('focus', () => activateItem(item));
  });

  function activateItem(targetItem) {
    navItems.forEach(nav => nav.classList.remove('active'));
    targetItem.classList.add('active');
    
    const targetId = targetItem.getAttribute('data-target');
    animations.forEach(anim => {
      if(anim.id === targetId) anim.classList.add('active');
      else anim.classList.remove('active');
    });
  }

  // Intersection Observer for scroll reveal
  const splitSection = document.getElementById('split-features');
  if(splitSection) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          // Disconnect observer after it runs once
          observer.disconnect();
        }
      });
    }, { threshold: 0.1 });
    observer.observe(splitSection);
  }
});
</script>
"""

new_content = content[:start_idx] + html_code + "\n" + content[end_idx:]
new_content = new_content.replace('</body>', js_code + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Split layout injected successfully.")
