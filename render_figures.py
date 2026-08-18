import os
from PIL import Image, ImageDraw, ImageFont

dest_dir = r"D:\\"
os.makedirs(dest_dir, exist_ok=True)

# -------------------------------------------------------------
# FIG 1: System Block Diagram (Numerals 100-122)
# -------------------------------------------------------------
img1_w, img1_h = 1600, 2200
img1 = Image.new('RGB', (img1_w, img1_h), color='#F8FAFC')
draw1 = ImageDraw.Draw(img1)

try:
    font_title = ImageFont.truetype("arial.ttf", 36)
    font_header = ImageFont.truetype("arial.ttf", 26)
    font_box = ImageFont.truetype("arial.ttf", 20)
    font_sub = ImageFont.truetype("arial.ttf", 16)
except Exception:
    font_title = font_header = font_box = font_sub = ImageFont.load_default()

# Main Title
draw1.text((50, 40), "FIG. 1 — SYSTEM BLOCK DIAGRAM", fill="#0F172A", font=font_title)
draw1.text((50, 85), "Architecture & Component Interaction (Numerals 100–122)", fill="#475569", font=font_header)

# Container 100: Client Device
draw1.rectangle([40, 140, 1560, 2120], outline="#1E293B", width=4, fill="#FFFFFF")
draw1.text((70, 160), "100 Client Device", fill="#1E293B", font=font_header)

# Container 102: Web Browser Runtime Environment
draw1.rectangle([70, 210, 1530, 2090], outline="#3B82F6", width=3, fill="#F0F9FF")
draw1.text((100, 230), "102 Web Browser Runtime Environment", fill="#1D4ED8", font=font_header)

boxes1 = [
    # (x1, y1, x2, y2, title, subtitle, bg)
    (120, 290, 770, 450, "104 Interactive Canvas & Input Module", "Mouse/Touch Events, Drag-and-Drop, Wiring", "#E0F2FE"),
    (830, 290, 1480, 450, "106 Component Library & Custom Gates", "Logic Primitives, Multiplexers, Custom ICs", "#E0F2FE"),
    
    (120, 520, 770, 680, "108 Custom Assembly Compiler", "compileASM() 3-Pass Macro & Label Resolver", "#FEF3C7"),
    (830, 520, 1480, 680, "110 Topological Sorting Processor", "topoSortGates() BFS Dependency Order", "#FEF3C7"),
    
    (120, 750, 770, 910, "112 CPU & ROM Emulation Engine", "Instruction Fetch, Memory-Mapped Bytecode", "#DCFCE7"),
    (830, 750, 1480, 910, "114 Signal Propagation Processor", "simulate() Iterative Boolean Gate Evaluator", "#DCFCE7"),
    
    (120, 980, 770, 1140, "116 HTML5 Canvas Engine (60 FPS)", "requestAnimationFrame Visual Renderer", "#F3E8FF"),
    (830, 980, 1480, 1140, "118 Waveform Signal Generator", "Timing Analysis & Oscilloscope Buffers", "#F3E8FF"),
    
    (120, 1210, 770, 1370, "120 State Serialization Module", "JSON Marshalling of Gates & Wires", "#FFEDD5"),
    (830, 1210, 1480, 1370, "121 Local Storage Persistence Engine", "Offline LocalStorage Storage Subsystem", "#FFEDD5"),
    
    (120, 1440, 1480, 1600, "122 Display Output (Visual UI)", "Interactive Canvas Monitor & Output Overlays", "#E2E8F0")
]

for b in boxes1:
    x1, y1, x2, y2, title, sub, bg = b
    draw1.rectangle([x1, y1, x2, y2], outline="#475569", width=2, fill=bg)
    draw1.text((x1 + 20, y1 + 25), title, fill="#0F172A", font=font_box)
    draw1.text((x1 + 20, y1 + 75), sub, fill="#475569", font=font_sub)

# Draw connecting arrows
def draw_arrow(draw, pt1, pt2, text=""):
    draw.line([pt1, pt2], fill="#0F172A", width=3)
    x2, y2 = pt2
    draw.polygon([(x2-8, y2-8), (x2+8, y2-8), (x2, y2)], fill="#0F172A")
    if text:
        tx = (pt1[0] + pt2[0]) // 2 + 10
        ty = (pt1[1] + pt2[1]) // 2 - 10
        draw.text((tx, ty), text, fill="#2563EB", font=font_sub)

# Arrows between boxes
draw_arrow(draw1, (445, 450), (445, 520), "Raw ASM Directives")
draw_arrow(draw1, (1155, 450), (1155, 520), "Component Graph")

draw_arrow(draw1, (445, 680), (445, 750), "256-Byte Bytecode")
draw_arrow(draw1, (1155, 680), (1155, 750), "Ordered Gate Array")

draw_arrow(draw1, (445, 910), (445, 980), "High / Low Signals")
draw_arrow(draw1, (1155, 910), (1155, 980), "Signal History Ticks")

draw_arrow(draw1, (445, 1140), (445, 1210), "State Object")
draw_arrow(draw1, (1155, 1140), (1155, 1210), "JSON String")

draw_arrow(draw1, (800, 1370), (800, 1440), "Render Frame")

fig1_path_png = os.path.join(dest_dir, "fig1_system_block_diagram.png")
img1.save(fig1_path_png)
print("Saved:", fig1_path_png)


# -------------------------------------------------------------
# FIG 2: Method Flowchart (Steps 202-216)
# -------------------------------------------------------------
img2_w, img2_h = 1400, 1800
img2 = Image.new('RGB', (img2_w, img2_h), color='#F8FAFC')
draw2 = ImageDraw.Draw(img2)

draw2.text((50, 40), "FIG. 2 — METHOD FLOWCHART", fill="#0F172A", font=font_title)
draw2.text((50, 85), "Simulation & Execution Method Steps (202–216)", fill="#475569", font=font_header)

steps = [
    ("202", "Start: Render Initial Workspace & Load Component Libraries", "#E2E8F0"),
    ("204", "Process User Inputs: Place Components & Connect Wires", "#DBEAFE"),
    ("205", "Determine Action Branch: Assembly Edit vs Canvas Circuit Edit", "#FEF3C7"),
    ("206", "Determine Gate Evaluation Order via Topological Sorting", "#E0E7FF"),
    ("208", "Compile Assembly Code, Resolve Labels & Flash Bytecode to ROM", "#FEF3C7"),
    ("210", "Execute Instruction Cycle & Compute Gate State Transitions", "#DCFCE7"),
    ("212", "Propagate Binary Signals & Update Wire States (High/Low)", "#DCFCE7"),
    ("214", "Generate Waveform Signal Data for Oscilloscope Panel", "#F3E8FF"),
    ("216", "Serialize State to LocalStorage & Render Display Output", "#FFEDD5")
]

start_y = 150
box_h = 100
gap = 60
x_mid = 700
box_w = 1000

for i, (num, text, bg) in enumerate(steps):
    y = start_y + i * (box_h + gap)
    x1 = x_mid - box_w // 2
    x2 = x_mid + box_w // 2
    y1 = y
    y2 = y + box_h
    
    # Draw box
    if num == "202":
        # Rounded pill shape for Start
        draw2.ellipse([x1, y1, x1+60, y2], fill=bg, outline="#475569", width=2)
        draw2.ellipse([x2-60, y1, x2, y2], fill=bg, outline="#475569", width=2)
        draw2.rectangle([x1+30, y1, x2-30, y2], fill=bg, outline=None)
        draw2.line([x1+30, y1, x2-30, y1], fill="#475569", width=2)
        draw2.line([x1+30, y2, x2-30, y2], fill="#475569", width=2)
    elif num == "205":
        # Diamond decision shape
        pts = [(x_mid, y1-10), (x2, y1 + box_h//2), (x_mid, y2+10), (x1, y1 + box_h//2)]
        draw2.polygon(pts, fill=bg, outline="#D97706", width=2)
    else:
        draw2.rectangle([x1, y1, x2, y2], outline="#475569", width=2, fill=bg)
        
    draw2.text((x1 + 30, y1 + 35), f"Step {num}:  {text}", fill="#0F172A", font=font_box)
    
    if i < len(steps) - 1:
        # Arrow down
        pt1 = (x_mid, y2 if num != "205" else y2+10)
        pt2 = (x_mid, y + box_h + gap)
        draw2.line([pt1, pt2], fill="#0F172A", width=3)
        draw2.polygon([(x_mid-8, pt2[1]-10), (x_mid+8, pt2[1]-10), (x_mid, pt2[1])], fill="#0F172A")

fig2_path_png = os.path.join(dest_dir, "fig2_method_flowchart.png")
img2.save(fig2_path_png)
print("Saved:", fig2_path_png)


# Also generate clean SVG files
svg1_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 2200" width="1600" height="2200" style="background:#F8FAFC;font-family:Arial,sans-serif;">
  <text x="50" y="50" font-size="36" font-weight="bold" fill="#0F172A">FIG. 1 — SYSTEM BLOCK DIAGRAM</text>
  <text x="50" y="90" font-size="24" fill="#475569">Architecture &amp; Component Interaction (Numerals 100–122)</text>
  
  <rect x="40" y="140" width="1520" height="1980" fill="#FFFFFF" stroke="#1E293B" stroke-width="4" rx="8"/>
  <text x="70" y="180" font-size="24" font-weight="bold" fill="#1E293B">100 Client Device</text>
  
  <rect x="70" y="210" width="1460" height="1880" fill="#F0F9FF" stroke="#3B82F6" stroke-width="3" rx="6"/>
  <text x="100" y="250" font-size="22" font-weight="bold" fill="#1D4ED8">102 Web Browser Runtime Environment</text>
  
  <!-- Boxes -->
  <g stroke="#475569" stroke-width="2" font-size="20">
    <rect x="120" y="290" width="650" height="160" fill="#E0F2FE" rx="6"/>
    <text x="140" y="340" font-weight="bold" fill="#0F172A" stroke="none">104 Interactive Canvas &amp; Input Module</text>
    <text x="140" y="380" font-size="16" fill="#475569" stroke="none">Mouse/Touch Events, Drag-and-Drop, Wiring</text>
    
    <rect x="830" y="290" width="650" height="160" fill="#E0F2FE" rx="6"/>
    <text x="850" y="340" font-weight="bold" fill="#0F172A" stroke="none">106 Component Library &amp; Custom Gates</text>
    <text x="850" y="380" font-size="16" fill="#475569" stroke="none">Logic Primitives, Multiplexers, Custom ICs</text>
    
    <rect x="120" y="520" width="650" height="160" fill="#FEF3C7" rx="6"/>
    <text x="140" y="570" font-weight="bold" fill="#0F172A" stroke="none">108 Custom Assembly Compiler</text>
    <text x="140" y="610" font-size="16" fill="#475569" stroke="none">compileASM() 3-Pass Macro &amp; Label Resolver</text>
    
    <rect x="830" y="520" width="650" height="160" fill="#FEF3C7" rx="6"/>
    <text x="850" y="570" font-weight="bold" fill="#0F172A" stroke="none">110 Topological Sorting Processor</text>
    <text x="850" y="610" font-size="16" fill="#475569" stroke="none">topoSortGates() BFS Dependency Order</text>
    
    <rect x="120" y="750" width="650" height="160" fill="#DCFCE7" rx="6"/>
    <text x="140" y="800" font-weight="bold" fill="#0F172A" stroke="none">112 CPU &amp; ROM Emulation Engine</text>
    <text x="140" y="840" font-size="16" fill="#475569" stroke="none">Instruction Fetch, Memory-Mapped Bytecode</text>
    
    <rect x="830" y="750" width="650" height="160" fill="#DCFCE7" rx="6"/>
    <text x="850" y="800" font-weight="bold" fill="#0F172A" stroke="none">114 Signal Propagation Processor</text>
    <text x="850" y="840" font-size="16" fill="#475569" stroke="none">simulate() Iterative Boolean Gate Evaluator</text>
    
    <rect x="120" y="980" width="650" height="160" fill="#F3E8FF" rx="6"/>
    <text x="140" y="1030" font-weight="bold" fill="#0F172A" stroke="none">116 HTML5 Canvas Engine (60 FPS)</text>
    <text x="140" y="1070" font-size="16" fill="#475569" stroke="none">requestAnimationFrame Visual Renderer</text>
    
    <rect x="830" y="980" width="650" height="160" fill="#F3E8FF" rx="6"/>
    <text x="850" y="1030" font-weight="bold" fill="#0F172A" stroke="none">118 Waveform Signal Generator</text>
    <text x="850" y="1070" font-size="16" fill="#475569" stroke="none">Timing Analysis &amp; Oscilloscope Buffers</text>
    
    <rect x="120" y="1210" width="650" height="160" fill="#FFEDD5" rx="6"/>
    <text x="140" y="1260" font-weight="bold" fill="#0F172A" stroke="none">120 State Serialization Module</text>
    <text x="140" y="1300" font-size="16" fill="#475569" stroke="none">JSON Marshalling of Gates &amp; Wires</text>
    
    <rect x="830" y="1210" width="650" height="160" fill="#FFEDD5" rx="6"/>
    <text x="850" y="1260" font-weight="bold" fill="#0F172A" stroke="none">121 Local Storage Persistence Engine</text>
    <text x="850" y="1300" font-size="16" fill="#475569" stroke="none">Offline LocalStorage Storage Subsystem</text>
    
    <rect x="120" y="1440" width="1360" height="160" fill="#E2E8F0" rx="6"/>
    <text x="140" y="1490" font-weight="bold" fill="#0F172A" stroke="none">122 Display Output (Visual UI)</text>
    <text x="140" y="1530" font-size="16" fill="#475569" stroke="none">Interactive Canvas Monitor &amp; Output Overlays</text>
  </g>
</svg>'''

with open(os.path.join(dest_dir, "fig1_system_block_diagram.svg"), "w") as f:
    f.write(svg1_content)
print("Saved SVG 1")

svg2_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 1800" width="1400" height="1800" style="background:#F8FAFC;font-family:Arial,sans-serif;">
  <text x="50" y="50" font-size="36" font-weight="bold" fill="#0F172A">FIG. 2 — METHOD FLOWCHART</text>
  <text x="50" y="90" font-size="24" fill="#475569">Simulation &amp; Execution Method Steps (202–216)</text>
  
  <g font-size="20" stroke="#475569" stroke-width="2">
    <!-- Step 202 -->
    <rect x="200" y="150" width="1000" height="100" rx="50" fill="#E2E8F0"/>
    <text x="230" y="210" font-weight="bold" fill="#0F172A" stroke="none">Step 202:  Start: Render Initial Workspace &amp; Load Component Libraries</text>
    
    <!-- Step 204 -->
    <rect x="200" y="310" width="1000" height="100" rx="6" fill="#DBEAFE"/>
    <text x="230" y="370" font-weight="bold" fill="#0F172A" stroke="none">Step 204:  Process User Inputs: Place Components &amp; Connect Wires</text>
    
    <!-- Step 205 -->
    <polygon points="700,460 1200,520 700,580 200,520" fill="#FEF3C7" stroke="#D97706"/>
    <text x="280" y="527" font-weight="bold" fill="#0F172A" stroke="none">Step 205:  Determine Action Branch: Assembly Edit vs Canvas Edit</text>
    
    <!-- Step 206 -->
    <rect x="200" y="630" width="1000" height="100" rx="6" fill="#E0E7FF"/>
    <text x="230" y="690" font-weight="bold" fill="#0F172A" stroke="none">Step 206:  Determine Gate Evaluation Order via Topological Sorting</text>
    
    <!-- Step 208 -->
    <rect x="200" y="790" width="1000" height="100" rx="6" fill="#FEF3C7"/>
    <text x="230" y="850" font-weight="bold" fill="#0F172A" stroke="none">Step 208:  Compile Assembly Code, Resolve Labels &amp; Flash Bytecode to ROM</text>
    
    <!-- Step 210 -->
    <rect x="200" y="950" width="1000" height="100" rx="6" fill="#DCFCE7"/>
    <text x="230" y="1010" font-weight="bold" fill="#0F172A" stroke="none">Step 210:  Execute Instruction Cycle &amp; Compute Gate State Transitions</text>
    
    <!-- Step 212 -->
    <rect x="200" y="1110" width="1000" height="100" rx="6" fill="#DCFCE7"/>
    <text x="230" y="1170" font-weight="bold" fill="#0F172A" stroke="none">Step 212:  Propagate Binary Signals &amp; Update Wire States (High/Low)</text>
    
    <!-- Step 214 -->
    <rect x="200" y="1270" width="1000" height="100" rx="6" fill="#F3E8FF"/>
    <text x="230" y="1330" font-weight="bold" fill="#0F172A" stroke="none">Step 214:  Generate Waveform Signal Data for Oscilloscope Panel</text>
    
    <!-- Step 216 -->
    <rect x="200" y="1430" width="1000" height="100" rx="6" fill="#FFEDD5"/>
    <text x="230" y="1490" font-weight="bold" fill="#0F172A" stroke="none">Step 216:  Serialize State to LocalStorage &amp; Render Display Output</text>
  </g>
</svg>'''

with open(os.path.join(dest_dir, "fig1_system_block_diagram.svg"), "w") as f:
    f.write(svg1_content)
with open(os.path.join(dest_dir, "fig2_method_flowchart.svg"), "w") as f:
    f.write(svg2_content)
print("Saved SVG 2")
