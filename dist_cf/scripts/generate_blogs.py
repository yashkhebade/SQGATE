import os
import json
import re
import shutil
import glob

# Find the generated images in the brain directory
brain_dir = r"C:\Users\Admin\.gemini\antigravity\brain\d8f91a6b-225f-4a7f-bcb0-42fef73b56f3"
image_files = glob.glob(os.path.join(brain_dir, "*.png"))

image_map = {}
for img in image_files:
    filename = os.path.basename(img)
    if filename.startswith("karnaugh_map_"): image_map["karnaugh_map"] = img
    elif filename.startswith("fsm_design_"): image_map["fsm_design"] = img
    elif filename.startswith("sequential_logic_"): image_map["sequential_logic"] = img
    elif filename.startswith("cmos_logic_"): image_map["cmos_logic"] = img
    elif filename.startswith("verilog_hdl_"): image_map["verilog_hdl"] = img
    elif filename.startswith("alu_8bit_"): image_map["alu_8bit"] = img
    elif filename.startswith("boolean_algebra_"): image_map["boolean_algebra"] = img
    elif filename.startswith("multiplexers_"): image_map["multiplexers"] = img

blog_data = [
    {
        "slug": "karnaugh-maps-intro",
        "title": "Introduction to Karnaugh Maps: Simplifying Logic Effortlessly",
        "desc": "Learn how to use Karnaugh Maps (K-Maps) to simplify complex boolean expressions visually and efficiently for digital logic design.",
        "keywords": "karnaugh map, k-map, boolean algebra, logic simplification, digital logic, sqgate",
        "author": "Yash Khebade",
        "date": "July 1, 2026",
        "read_time": "5 min read",
        "image_key": "karnaugh_map",
        "tags": "Logic Design",
        "content": """
            <h2>What is a Karnaugh Map?</h2>
            <p>A Karnaugh Map (K-map) is a visual method used to simplify boolean algebra expressions. Invented by Maurice Karnaugh in 1953, it transforms a truth table into a 2D grid where adjacent cells represent boolean variables that differ by only one bit (Gray code).</p>
            <h3>Why use K-Maps?</h3>
            <p>While boolean algebra rules can simplify expressions, it's often tedious and error-prone. K-maps provide a straightforward visual pattern-matching approach to find the minimal sum-of-products (SOP) or product-of-sums (POS).</p>
            <h3>How it works</h3>
            <p>To use a K-map, you group adjacent 1s in powers of 2 (1, 2, 4, 8). The larger the group, the more variables you eliminate. SQGATE provides an automated Karnaugh Map solver that visualizes these groupings for you instantly.</p>
        """
    },
    {
        "slug": "fsm-design-javascript",
        "title": "Mastering Finite State Machines (FSMs) in Hardware Design",
        "desc": "A comprehensive guide to designing Moore and Mealy Finite State Machines for digital circuits and simulating them.",
        "keywords": "finite state machine, FSM, moore machine, mealy machine, digital logic, state diagram",
        "author": "SQGATE Engineering",
        "date": "July 1, 2026",
        "read_time": "8 min read",
        "image_key": "fsm_design",
        "tags": "Advanced",
        "content": """
            <h2>The Brains of Sequential Logic</h2>
            <p>A Finite State Machine (FSM) is a mathematical model of computation used to design both computer programs and sequential logic circuits. It consists of a finite number of states, transitions between those states, and actions.</p>
            <h3>Moore vs. Mealy</h3>
            <ul>
                <li><strong>Moore Machine:</strong> The outputs are determined solely by the current state.</li>
                <li><strong>Mealy Machine:</strong> The outputs are determined by the current state AND the current inputs.</li>
            </ul>
            <p>FSMs are essential for designing control units in CPUs, traffic light controllers, and vending machines.</p>
        """
    },
    {
        "slug": "sequential-logic-demystified",
        "title": "Sequential Logic Demystified: D-Flip Flops and Latches",
        "desc": "Understand the core building blocks of computer memory: latches and flip-flops, and how sequential logic differs from combinational logic.",
        "keywords": "sequential logic, d-flip flop, sr latch, memory, clock signal, digital circuits",
        "author": "Yash Khebade",
        "date": "July 1, 2026",
        "read_time": "6 min read",
        "image_key": "sequential_logic",
        "tags": "Memory",
        "content": """
            <h2>Combinational vs. Sequential</h2>
            <p>Combinational logic outputs depend strictly on current inputs (like an AND gate). Sequential logic outputs depend on current inputs AND the past history of inputs. This history is stored as "state".</p>
            <h3>The SR Latch</h3>
            <p>The simplest memory element is the Set-Reset (SR) latch, created by cross-coupling two NOR or NAND gates. However, it suffers from a race condition if both S and R are triggered simultaneously.</p>
            <h3>The D-Flip Flop</h3>
            <p>To solve timing issues, we use the D-Flip Flop, which captures the value of the Data (D) input exclusively on the rising or falling edge of a Clock signal. This is the fundamental unit of registers and RAM in modern CPUs.</p>
        """
    },
    {
        "slug": "cmos-logic-gates",
        "title": "CMOS Logic Gates: The Foundation of Modern Electronics",
        "desc": "Explore how Complementary Metal-Oxide-Semiconductors (CMOS) are used to build logic gates at the physical transistor level.",
        "keywords": "CMOS, transistors, logic gates, PMOS, NMOS, semiconductor, VLSI",
        "author": "SQGATE Engineering",
        "date": "July 1, 2026",
        "read_time": "7 min read",
        "image_key": "cmos_logic",
        "tags": "Hardware",
        "content": """
            <h2>The Magic of CMOS</h2>
            <p>Complementary Metal-Oxide-Semiconductor (CMOS) technology is used for constructing integrated circuits. It uses a combination of p-type (PMOS) and n-type (NMOS) MOSFETs.</p>
            <h3>Why CMOS?</h3>
            <p>CMOS devices have high noise immunity and low static power consumption. Since one transistor of the pair is always off, the series combination draws significant power only momentarily during switching between on and off states.</p>
            <h3>Building an Inverter (NOT Gate)</h3>
            <p>The simplest CMOS gate is the inverter. It consists of one PMOS transistor connected to the power supply (Vdd) and one NMOS connected to ground (GND). When the input is HIGH, the NMOS turns on, pulling the output LOW. When the input is LOW, the PMOS turns on, pulling the output HIGH.</p>
        """
    },
    {
        "slug": "from-schematic-to-verilog",
        "title": "From Schematic to Verilog: A Beginner's Guide",
        "desc": "Learn how to transition from drawing visual logic schematics to writing professional Verilog Hardware Description Language (HDL).",
        "keywords": "verilog, HDL, schematic, digital design, FPGA, logic synthesis, sqgate",
        "author": "Yash Khebade",
        "date": "July 1, 2026",
        "read_time": "6 min read",
        "image_key": "verilog_hdl",
        "tags": "Verilog",
        "content": """
            <h2>What is Verilog?</h2>
            <p>Verilog is a Hardware Description Language (HDL) used to model electronic systems. Unlike programming languages (C++, Python) which execute sequentially, HDL code executes concurrently, mapping directly to physical logic gates and wires.</p>
            <h3>Structural vs. Behavioral</h3>
            <ul>
                <li><strong>Structural:</strong> Defining the exact gates and how they wire together (netlists).</li>
                <li><strong>Behavioral:</strong> Describing the algorithmic function (e.g., `if (a > b)`) and letting a synthesizer figure out the gates.</li>
            </ul>
            <p>SQGATE includes a one-click Verilog Exporter that instantly translates your visual drag-and-drop schematics into valid Structural Verilog, making it the perfect learning bridge for FPGA students!</p>
        """
    },
    {
        "slug": "architecting-8bit-alu",
        "title": "Architecting an 8-bit ALU: Building the Brain of a CPU",
        "desc": "A step-by-step architectural breakdown of designing an 8-bit Arithmetic Logic Unit from basic logic gates.",
        "keywords": "ALU, arithmetic logic unit, CPU architecture, 8-bit, full adder, logic design",
        "author": "SQGATE Engineering",
        "date": "July 1, 2026",
        "read_time": "9 min read",
        "image_key": "alu_8bit",
        "tags": "Architecture",
        "content": """
            <h2>The Core of Computation</h2>
            <p>The Arithmetic Logic Unit (ALU) is the part of a CPU that performs all mathematical and logical operations. It takes two operands (like A and B) and an opcode (instruction) to determine what operation to perform.</p>
            <h3>Components of an ALU</h3>
            <p>An 8-bit ALU typically includes:</p>
            <ul>
                <li><strong>Adders:</strong> 8 Full Adders chained together (ripple carry) or using Look-Ahead Carry logic for speed.</li>
                <li><strong>Logic Blocks:</strong> Arrays of AND, OR, and XOR gates applied bitwise to the operands.</li>
                <li><strong>Multiplexers:</strong> A massive MUX array at the output that selects which result (the sum, the AND result, etc.) gets passed to the final output based on the opcode.</li>
            </ul>
            <p>You can build and simulate a full 8-bit ALU right inside the SQGATE simulator using our advanced bus splitters and combinational primitives.</p>
        """
    },
    {
        "slug": "boolean-algebra-hacks",
        "title": "Boolean Algebra Hacks for Computer Engineering Students",
        "desc": "Essential tricks, theorems, and shortcuts for simplifying boolean expressions on your next digital logic exam.",
        "keywords": "boolean algebra, De Morgan's laws, logic simplification, engineering hacks",
        "author": "Yash Khebade",
        "date": "July 1, 2026",
        "read_time": "5 min read",
        "image_key": "boolean_algebra",
        "tags": "Theory",
        "content": """
            <h2>Mastering the Math of Logic</h2>
            <p>Boolean algebra is the mathematical foundation of digital circuits. While K-maps are great visually, knowing the algebraic theorems is crucial for exams and quick optimizations.</p>
            <h3>De Morgan's Laws</h3>
            <p>The most important hack in your arsenal: "Break the line, change the sign."</p>
            <code>~(A * B) = ~A + ~B</code><br>
            <code>~(A + B) = ~A * ~B</code>
            <p>This allows you to convert NAND gates to OR gates with inverted inputs, which is critical for CMOS layout optimization.</p>
            <h3>The Consensus Theorem</h3>
            <p>Often overlooked, the consensus theorem can instantly simplify tricky expressions: <code>AB + ~AC + BC = AB + ~AC</code>. The `BC` term is redundant!</p>
        """
    },
    {
        "slug": "multiplexers-demultiplexers",
        "title": "Multiplexers and Demultiplexers: Routing Data in Hardware",
        "desc": "Understand how MUX and DEMUX components act as the digital switches of hardware architecture.",
        "keywords": "multiplexer, demultiplexer, MUX, data routing, digital switches, logic design",
        "author": "SQGATE Engineering",
        "date": "July 1, 2026",
        "read_time": "6 min read",
        "image_key": "multiplexers",
        "tags": "Components",
        "content": """
            <h2>The Digital Train Switch</h2>
            <p>A Multiplexer (MUX) is a combinational circuit that selects one of many input signals and forwards the selected input into a single line. It is controlled by a set of 'select lines'.</p>
            <h3>How a 2-to-1 MUX Works</h3>
            <p>A 2-to-1 MUX has two inputs (A and B) and one select line (S). The boolean equation is: <code>Output = (A * ~S) + (B * S)</code>. If S is 0, A passes through. If S is 1, B passes through.</p>
            <h3>Demultiplexers (DEMUX)</h3>
            <p>A DEMUX does the exact opposite: it takes a single input and routes it to one of many outputs. Together, MUX and DEMUX components are used extensively in CPU buses, memory addressing, and data communication networks.</p>
        """
    }
]

import os, json

# Paths
blog_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog"
template_path = os.path.join(blog_dir, "template.html")
index_path = os.path.join(blog_dir, "index.html")
posts_dir = os.path.join(blog_dir, "posts")
assets_dir = os.path.join(blog_dir, "assets")

os.makedirs(posts_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)

with open(template_path, "r", encoding="utf-8") as f:
    template_html = f.read()

# Fix og:image in template if not already a variable
if 'content="https://sqgate.online/og-image.png"' in template_html:
    template_html = template_html.replace('content="https://sqgate.online/og-image.png"', 'content="{{OG_IMAGE}}"')

cards_html = ""

for post in blog_data:
    # 1. Copy Image
    src_img = image_map.get(post["image_key"])
    dest_img_name = post["slug"] + ".png"
    dest_img_path = os.path.join(assets_dir, dest_img_name)
    if src_img and os.path.exists(src_img):
        shutil.copy(src_img, dest_img_path)
    
    # 2. Build Schema JSON
    schema_json = json.dumps({
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": f"https://sqgate.online/blog/posts/{post['slug']}.html"
      },
      "headline": post["title"],
      "image": f"https://sqgate.online/blog/assets/{post['slug']}.png",  
      "author": {
        "@type": "Person",
        "name": post["author"]
      },  
      "publisher": {
        "@type": "Organization",
        "name": "SQGATE",
        "logo": {
          "@type": "ImageObject",
          "url": "https://sqgate.online/icon.png"
        }
      },
      "datePublished": "2026-07-01"
    }, indent=2)

    # 3. Inject variables into template
    html = template_html
    html = html.replace("{{META_TITLE}}", f"{post['title']} | SQGATE Blog")
    html = html.replace("{{META_DESCRIPTION}}", post["desc"])
    html = html.replace("{{META_KEYWORDS}}", post["keywords"])
    html = html.replace("{{CANONICAL_URL}}", f"https://sqgate.online/blog/posts/{post['slug']}.html")
    html = html.replace("{{OG_IMAGE}}", f"https://sqgate.online/blog/assets/{post['slug']}.png")
    html = html.replace("{{SCHEMA_JSON}}", schema_json)
    html = html.replace("{{TITLE}}", post["title"])
    html = html.replace("{{AUTHOR}}", post["author"])
    html = html.replace("{{DATE}}", post["date"])
    html = html.replace("{{READ_TIME}}", post["read_time"])
    html = html.replace("{{CONTENT}}", post["content"])
    
    # 4. Save HTML
    out_path = os.path.join(posts_dir, f"{post['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    # 5. Build card HTML for index
    card = f"""
    <a href="/blog/posts/{post['slug']}.html" class="card">
      <div class="card-img-container">
        <img src="/blog/assets/{post['slug']}.png" alt="{post['title']}" class="card-img" loading="lazy">
      </div>
      <div class="card-content">
        <div class="card-tag">{post['tags']}</div>
        <h3 class="card-title">{post['title']}</h3>
        <p class="card-desc">{post['desc']}</p>
        <div class="card-meta">
          <span>{post['date']}</span>
          <span>{post['read_time']}</span>
        </div>
      </div>
    </a>
    """
    cards_html += card

# Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Replace the grid content in index.html
grid_start = index_html.find('<div class="grid">')
if grid_start != -1:
    grid_end = index_html.find('</div>', grid_start)
    if grid_end != -1:
        new_grid = f'<div class="grid">\n{cards_html}\n    </div>'
        index_html = index_html[:grid_start] + new_grid + index_html[grid_end+6:]
        
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
    
print("Successfully generated 8 blog posts, copied images, and updated index.html!")
