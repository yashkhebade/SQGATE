import os
import shutil
import re
import datetime

artifact_dir = r"C:\Users\Admin\.gemini\antigravity\brain\d8f91a6b-225f-4a7f-bcb0-42fef73b56f3"
workspace_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"
blog_dir = os.path.join(workspace_dir, "blog")
posts_dir = os.path.join(blog_dir, "posts")
images_dir = os.path.join(posts_dir, "images")
template_path = os.path.join(blog_dir, "template.html")

os.makedirs(images_dir, exist_ok=True)

# Image mapping
image_files = {
    "flip-flops-explained.html": "blog_flip_flops_1783064185971.png",
    "intro-to-k-maps.html": "blog_karnaugh_maps_1783064197529.png",
    "multiplexer-routing.html": "blog_multiplexers_1783064207922.png",
    "shift-registers-guide.html": "blog_shift_registers_1783064289632.png",
    "cmos-logic-gates.html": "blog_cmos_gates_1783064300887.png",
    "digital-counters-guide.html": "blog_digital_counters_1783064228484.png",
    "fsm-moore-mealy.html": "blog_fsm_machines_1783064238505.png",
    "boolean-algebra-laws.html": "blog_boolean_algebra_1783064249417.png",
    "alu-twos-complement.html": "blog_alu_twos_complement_1783064261528.png",
    "fpga-basics-intro.html": "blog_fpga_basics_1783064271340.png",
}

for dest, src in image_files.items():
    src_path = os.path.join(artifact_dir, src)
    if os.path.exists(src_path):
        shutil.copy(src_path, os.path.join(images_dir, src))

posts = [
    {
        "filename": "flip-flops-explained.html",
        "title": "Demystifying Flip-Flops: SR, D, JK, and T",
        "meta_title": "Flip-Flops Explained: SR, D, JK & T Types | SQGATE",
        "meta_desc": "A complete guide to digital flip-flops. Learn the differences between SR, D, JK, and T flip-flops and how they store data in memory circuits.",
        "meta_kw": "flip-flop, digital logic, sr flip flop, d flip flop, jk flip flop, t flip flop, memory",
        "read_time": "7 min read",
        "content": """
<h2>Introduction to Sequential Logic</h2>
<p>Unlike combinational logic (where the output depends solely on current inputs), sequential logic circuits possess memory. Their output depends on both current inputs and the previous state. The fundamental building block of this memory is the flip-flop.</p>

<h2>The SR Flip-Flop (Set-Reset)</h2>
<p>The simplest flip-flop is the SR (Set-Reset) latch, typically built using cross-coupled NOR or NAND gates. When the Set (S) input is high, the output Q becomes 1. When Reset (R) is high, Q becomes 0. A major limitation is the invalid state when both S and R are high simultaneously.</p>

<h2>The D Flip-Flop (Data or Delay)</h2>
<p>To solve the SR flip-flop's invalid state issue, the D flip-flop introduces a single Data (D) input. The D input is fed directly to the S input, and an inverted copy is fed to the R input. This ensures S and R are never both high. On a clock edge, the D flip-flop simply captures the value of D and holds it until the next clock pulse. This makes it perfect for registers and memory storage.</p>

<h2>The JK Flip-Flop</h2>
<p>The JK flip-flop is the most versatile. It acts like an SR flip-flop (J=Set, K=Reset), but solves the invalid state condition. When both J and K are high, instead of becoming invalid, the JK flip-flop "toggles" its output, changing from 1 to 0 or 0 to 1 on every clock edge.</p>

<h2>The T Flip-Flop (Toggle)</h2>
<p>The T flip-flop is a single-input version of the JK flip-flop where J and K are tied together. If T is high, the output toggles on every clock edge. If T is low, the output retains its state. This makes it incredibly useful for building digital counters and frequency dividers.</p>
"""
    },
    {
        "filename": "intro-to-k-maps.html",
        "title": "Introduction to Karnaugh Maps for Beginners",
        "meta_title": "Karnaugh Maps (K-Maps) Tutorial | Boolean Simplification",
        "meta_desc": "Learn how to use Karnaugh Maps (K-Maps) to visually simplify complex boolean algebra expressions. A step-by-step guide for digital logic students.",
        "meta_kw": "karnaugh map, k-map, boolean algebra, logic minimization, sum of products, SOP",
        "read_time": "8 min read",
        "content": """
<h2>Why Do We Need Karnaugh Maps?</h2>
<p>Boolean algebra provides laws and theorems to simplify logic expressions, reducing the number of gates required to build a circuit. However, algebraic simplification can be unintuitive and prone to human error. Karnaugh Maps (K-Maps) offer a visual, systematic method to simplify boolean expressions without relying on complex algebraic gymnastics.</p>

<h2>How a K-Map Works</h2>
<p>A K-Map is essentially a 2D grid representation of a truth table. The grid is arranged in Gray code order, meaning only one bit changes between any two adjacent cells (horizontally or vertically). This specific arrangement ensures that adjacent cells represent minterms that differ by only a single variable.</p>

<h2>Grouping 1s</h2>
<p>The core process of K-Map simplification involves plotting the 1s from your truth table onto the grid, and then circling adjacent 1s into groups. The rules for grouping are strict:</p>
<ul>
    <li>Groups must be rectangular.</li>
    <li>The number of cells in a group must be a power of 2 (1, 2, 4, 8, 16).</li>
    <li>Groups can wrap around the edges of the map (top to bottom, left to right).</li>
    <li>You must make the groups as large as possible.</li>
</ul>

<h2>Deriving the Simplified Expression</h2>
<p>Once you have identified all the optimal groups, you write down the product term for each group. You look at the variables for the rows and columns that span the entire group. If a variable changes its state (e.g., from A to NOT A) within the group, it is eliminated. The variables that remain constant form the term. Finally, you OR these product terms together to get the simplified Sum of Products (SOP) expression.</p>
"""
    },
    {
        "filename": "multiplexer-routing.html",
        "title": "The Magic of Multiplexers (MUX) in Digital Routing",
        "meta_title": "Understanding Multiplexers (MUX) | Digital Routing",
        "meta_desc": "Discover how multiplexers (MUX) act as digital switches, routing multiple input signals to a single output line, and how to build logic functions with them.",
        "meta_kw": "multiplexer, MUX, digital switch, data routing, combinational logic",
        "read_time": "6 min read",
        "content": """
<h2>What is a Multiplexer?</h2>
<p>A multiplexer, or MUX, is the digital equivalent of a multi-way switch. It has multiple data inputs, a single data output, and a set of select lines. Based on the binary value applied to the select lines, the MUX connects exactly one of the data inputs to the output.</p>

<h2>The 2-to-1 MUX</h2>
<p>The simplest MUX is the 2-to-1 multiplexer. It has two data inputs (D0 and D1), one select line (S), and one output (Y). If S is 0, D0 is routed to Y. If S is 1, D1 is routed to Y. Internally, a 2-to-1 MUX is built using two AND gates, one OR gate, and an inverter.</p>

<h2>Scaling Up: 4-to-1, 8-to-1, and Beyond</h2>
<p>By adding more select lines, we can increase the number of inputs. A 4-to-1 MUX requires 2 select lines, an 8-to-1 MUX requires 3 select lines, and a $2^n$-to-1 MUX requires $n$ select lines. Multiplexers are essential in CPU design, particularly in the Arithmetic Logic Unit (ALU) to select which mathematical operation result should be outputted.</p>

<h2>Implementing Logic Functions with a MUX</h2>
<p>A fascinating property of multiplexers is that they can be used to implement ANY boolean logic function. For example, an 8-to-1 MUX can implement any 3-variable truth table without needing any external AND, OR, or NOT gates. You simply connect the truth table's variables to the MUX's select lines, and tie the MUX's data inputs to either VCC (1) or Ground (0) matching the output column of the truth table!</p>
"""
    },
    {
        "filename": "shift-registers-guide.html",
        "title": "Understanding Shift Registers and Data Serialization",
        "meta_title": "Shift Registers: SISO, SIPO, PISO, PIPO | Digital Logic",
        "meta_desc": "A comprehensive guide to Shift Registers. Learn how SISO, SIPO, PISO, and PIPO configurations work for data serialization and storage.",
        "meta_kw": "shift register, SISO, SIPO, PISO, PIPO, data serialization, flip-flops",
        "read_time": "8 min read",
        "content": """
<h2>What is a Shift Register?</h2>
<p>A shift register is a type of sequential logic circuit composed of a chain of flip-flops connected in cascade. With every clock pulse, data is shifted from one flip-flop to the next. They are primarily used for temporary data storage and for converting data between serial and parallel formats.</p>

<h2>SISO: Serial-In, Serial-Out</h2>
<p>In a SISO shift register, data is fed in one bit at a time (serially), and read out one bit at a time from the last flip-flop. It acts as a digital delay line. If you have an 8-bit SISO register, it takes 8 clock cycles for a bit to travel from the input to the output.</p>

<h2>SIPO: Serial-In, Parallel-Out</h2>
<p>A SIPO register is used to convert a serial data stream into a parallel data word. Data is shifted in serially, but all flip-flop outputs are accessible simultaneously. This is incredibly useful in communication protocols like SPI or UART, where data is transmitted over a single wire but needs to be processed as whole bytes by a microcontroller.</p>

<h2>PISO: Parallel-In, Serial-Out</h2>
<p>The inverse of SIPO, a PISO register takes a parallel data word and shifts it out one bit at a time on a single wire. It requires a load control signal to asynchronously latch the parallel data into the flip-flops before shifting begins. This is used in transmitters to serialize data before sending it over a cable.</p>

<h2>PIPO: Parallel-In, Parallel-Out</h2>
<p>A PIPO register loads all bits simultaneously and can be read simultaneously. It does not actually shift data. It simply acts as a standard data register or buffer for temporary storage.</p>
"""
    },
    {
        "filename": "cmos-logic-gates.html",
        "title": "CMOS Logic Gates: How Transistors Build Logic",
        "meta_title": "CMOS Logic Gates Explained: NMOS and PMOS | SQGATE",
        "meta_desc": "Understand the physical reality of digital logic. Learn how NMOS and PMOS transistors are arranged in a CMOS configuration to build NAND and NOR gates.",
        "meta_kw": "CMOS, NMOS, PMOS, transistor, logic gate, semiconductor, VLSI",
        "read_time": "9 min read",
        "content": """
<h2>The Illusion of 1s and 0s</h2>
<p>In digital design, we abstract away the physical reality by talking about 1s and 0s. But beneath the mathematical abstraction of Boolean algebra lies the physical reality of semiconductors, specifically MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors).</p>

<h2>NMOS and PMOS Transistors</h2>
<p>A MOSFET acts as an electrically controlled switch. There are two primary types used in digital logic:</p>
<ul>
    <li><strong>NMOS:</strong> Turns ON (conducts current) when a high voltage (Logic 1) is applied to its gate. It is excellent at pulling outputs down to Ground (Logic 0).</li>
    <li><strong>PMOS:</strong> Turns ON when a low voltage (Logic 0) is applied to its gate. It is excellent at pulling outputs up to VDD (Logic 1).</li>
</ul>

<h2>The CMOS Architecture</h2>
<p>Complementary MOS (CMOS) is the dominant technology for modern integrated circuits. It pairs a "pull-up" network of PMOS transistors with a "pull-down" network of NMOS transistors. The beauty of CMOS is that in any stable logic state, only one network is active. This means there is no direct path from VDD to Ground, resulting in near-zero static power consumption.</p>

<h2>Building a NAND Gate</h2>
<p>A CMOS NAND gate is built using two PMOS transistors in parallel (connected to VDD) and two NMOS transistors in series (connected to Ground). If both inputs are High, both NMOS transistors turn on, pulling the output Low (0). If either input is Low, the series NMOS path is broken, and at least one parallel PMOS transistor turns on, pulling the output High (1).</p>
"""
    },
    {
        "filename": "digital-counters-guide.html",
        "title": "Synchronous vs Asynchronous Counters",
        "meta_title": "Digital Counters: Synchronous vs Asynchronous | SQGATE",
        "meta_desc": "A complete guide to digital counters. Understand the differences, advantages, and timing issues between asynchronous ripple counters and synchronous counters.",
        "meta_kw": "digital counter, asynchronous counter, ripple counter, synchronous counter, flip-flop",
        "read_time": "7 min read",
        "content": """
<h2>What are Digital Counters?</h2>
<p>Counters are sequential logic circuits used to count pulses, measure time, or sequence operations. They are constructed by cascading multiple flip-flops together. The two main categories of counters are asynchronous and synchronous.</p>

<h2>Asynchronous (Ripple) Counters</h2>
<p>In an asynchronous counter, only the very first flip-flop is clocked by the external clock signal. The output of the first flip-flop acts as the clock input for the second flip-flop, and so on. The clock signal "ripples" through the chain.</p>
<p><strong>Pros:</strong> Very simple to design and requires minimal hardware.<br>
<strong>Cons:</strong> Because the clock must propagate through each flip-flop sequentially, propagation delays accumulate. This causes timing issues known as "glitches" or "race conditions" at high frequencies, as the counter momentarily enters incorrect intermediate states.</p>

<h2>Synchronous Counters</h2>
<p>In a synchronous counter, every single flip-flop is connected to the exact same external clock signal. All flip-flops trigger simultaneously on the clock edge. The counting logic is handled by a network of combinational logic gates (usually AND gates and XOR gates) connected to the flip-flop inputs.</p>
<p><strong>Pros:</strong> Extremely fast and completely eliminates the cumulative propagation delay and glitching issues of ripple counters.<br>
<strong>Cons:</strong> Requires more complex combinational logic, making the circuit physically larger and more difficult to design by hand for high bit counts.</p>
"""
    },
    {
        "filename": "fsm-moore-mealy.html",
        "title": "Understanding Finite State Machines (Moore vs. Mealy)",
        "meta_title": "Finite State Machines: Moore vs Mealy FSM | SQGATE",
        "meta_desc": "A deep dive into Finite State Machines (FSM). Learn the theoretical and practical differences between Moore and Mealy state machine architectures.",
        "meta_kw": "FSM, finite state machine, moore machine, mealy machine, state diagram, digital logic",
        "read_time": "8 min read",
        "content": """
<h2>What is an FSM?</h2>
<p>A Finite State Machine (FSM) is a mathematical model of computation used to design both computer programs and sequential logic circuits. An FSM consists of a finite number of states, transitions between those states, and actions. At any given moment, the machine can only be in one state.</p>

<h2>The Moore Machine</h2>
<p>In a Moore machine, the outputs depend <strong>ONLY on the current state</strong>. The outputs are associated directly with the state nodes in a state diagram. Because outputs change only when the state changes (which happens on a clock edge), Moore machines are inherently synchronous and their outputs are stable and isolated from immediate input fluctuations.</p>
<p>However, Moore machines often require more states to model a system than a Mealy machine, because output variations must be encoded as entirely new states.</p>

<h2>The Mealy Machine</h2>
<p>In a Mealy machine, the outputs depend on <strong>both the current state AND the current inputs</strong>. The outputs are associated with the transitions (arrows) between states. Because inputs can change asynchronously, the outputs of a Mealy machine can change asynchronously during a clock cycle.</p>
<p>Mealy machines typically require fewer states than Moore machines to model the same logic, making them more hardware-efficient. However, because their outputs can glitch if the inputs are noisy, they require careful timing analysis and often need output registers to synchronize the final signals.</p>
"""
    },
    {
        "filename": "boolean-algebra-laws.html",
        "title": "Boolean Algebra Laws and Theorems",
        "meta_title": "Boolean Algebra Laws, Theorems & Simplification | SQGATE",
        "meta_desc": "Master the fundamentals of Boolean algebra. A complete cheat sheet on De Morgan's Laws, absorption, consensus theorem, and algebraic simplification.",
        "meta_kw": "boolean algebra, de morgan's laws, boolean theorems, logic simplification, digital electronics",
        "read_time": "6 min read",
        "content": """
<h2>The Foundation of Digital Logic</h2>
<p>Boolean algebra, developed by George Boole in the 1850s, forms the mathematical bedrock of all digital electronics. Unlike standard algebra which uses continuous numbers, Boolean algebra operates entirely on two states: 1 (True) and 0 (False).</p>

<h2>Basic Postulates</h2>
<ul>
    <li><strong>Identity:</strong> A + 0 = A, and A · 1 = A</li>
    <li><strong>Null:</strong> A + 1 = 1, and A · 0 = 0</li>
    <li><strong>Idempotent:</strong> A + A = A, and A · A = A</li>
    <li><strong>Inverse:</strong> A + NOT(A) = 1, and A · NOT(A) = 0</li>
</ul>

<h2>Commutative, Associative, and Distributive Laws</h2>
<p>These laws mirror standard algebra. A + B = B + A. A(BC) = (AB)C. And crucially, A(B + C) = AB + AC. However, Boolean algebra has a unique distributive law: A + BC = (A + B)(A + C).</p>

<h2>De Morgan's Laws</h2>
<p>Augustus De Morgan formulated two laws that are arguably the most important tools for digital designers, allowing you to convert AND gates to OR gates and vice versa. They state:</p>
<ol>
    <li>The inverse of a sum is equal to the product of the inverses: <strong>NOT(A + B) = NOT(A) · NOT(B)</strong></li>
    <li>The inverse of a product is equal to the sum of the inverses: <strong>NOT(A · B) = NOT(A) + NOT(B)</strong></li>
</ol>
<p>These laws are physically responsible for why NAND and NOR gates are considered "universal gates."</p>
"""
    },
    {
        "filename": "alu-twos-complement.html",
        "title": "Arithmetic Logic Unit: Signed Numbers & Two's Complement",
        "meta_title": "Two's Complement & Signed Binary Arithmetic | SQGATE",
        "meta_desc": "Discover how computers handle negative numbers using Two's Complement representation, and how an ALU performs subtraction using only addition.",
        "meta_kw": "twos complement, two's complement, signed binary, ALU subtraction, digital arithmetic",
        "read_time": "9 min read",
        "content": """
<h2>The Problem of Negative Numbers</h2>
<p>A standard 8-bit binary register can hold values from 00000000 (0) to 11111111 (255). But how do we represent negative numbers? If we dedicate the most significant bit (MSB) as a sign bit (0 for positive, 1 for negative), we run into a major issue: arithmetic doesn't work naturally. Adding $+2 (00000010)$ and $-2 (10000010)$ using a standard adder circuit yields $10000100 (-4)$, not zero.</p>

<h2>The Genius of Two's Complement</h2>
<p>Two's complement is a mathematical encoding that solves this problem elegantly. To find the two's complement of a binary number, you invert all the bits (one's complement) and then add 1.</p>
<p>In an 8-bit two's complement system, values range from -128 to +127. The MSB still indicates the sign, but the beauty is that <strong>addition works perfectly without modifying the hardware adder</strong>. If you add $+2 (00000010)$ and $-2 (11111110)$ in two's complement, the result is $00000000$, with a carry out that is simply discarded.</p>

<h2>Subtraction via Addition</h2>
<p>Because of Two's Complement, an Arithmetic Logic Unit (ALU) does not need a separate subtractor circuit. To perform A - B, the ALU simply calculates A + (Two's Complement of B). To implement this in hardware, the ALU passes the B input through XOR gates (which invert B if the subtraction control line is high) and feeds the subtraction control line directly into the Carry-In of the adder to add the required +1.</p>
"""
    },
    {
        "filename": "fpga-basics-intro.html",
        "title": "FPGA Basics: What is a Field Programmable Gate Array?",
        "meta_title": "Introduction to FPGAs: LUTs, Routing and HDL | SQGATE",
        "meta_desc": "A beginner's introduction to Field Programmable Gate Arrays (FPGAs). Learn how LUTs and routing matrices allow software to define physical hardware.",
        "meta_kw": "FPGA, Field Programmable Gate Array, LUT, Lookup Table, Verilog, VHDL, digital design",
        "read_time": "10 min read",
        "content": """
<h2>The Chasm Between Software and Hardware</h2>
<p>Microcontrollers (like Arduinos) run software sequentially. They are highly flexible but relatively slow because they must fetch, decode, and execute instructions one by one. Application-Specific Integrated Circuits (ASICs) are custom silicon chips built for one specific task. They are incredibly fast but cannot be modified once manufactured.</p>
<p>Field Programmable Gate Arrays (FPGAs) sit perfectly in the middle. They offer the blazing speed of custom hardware with the reprogrammable flexibility of software.</p>

<h2>The Secret Ingredient: The LUT</h2>
<p>An FPGA does not contain massive arrays of physical AND and OR gates. Instead, it relies on Lookup Tables (LUTs). A 4-input LUT is essentially a tiny 16-bit SRAM memory block. By programming specific 1s and 0s into this memory, the LUT can imitate ANY 4-input logic gate or truth table imaginable. When you provide inputs to the LUT, it simply looks up the programmed output value.</p>

<h2>Routing Matrices</h2>
<p>An FPGA chip contains hundreds of thousands of these LUTs, alongside dedicated flip-flops and DSP slices. Connecting them together is a massive programmable routing matrix. When you "compile" code for an FPGA, the synthesis tool determines what data goes into which LUTs, and switches on microscopic transistors in the routing matrix to wire everything together.</p>

<h2>Hardware Description Languages (HDLs)</h2>
<p>You don't program FPGAs with C or Python. You design circuits for them using Hardware Description Languages like Verilog or VHDL. These languages allow you to describe parallel hardware architectures, which the synthesis tool then maps onto the physical LUTs and routing resources of the chip.</p>
"""
    }
]

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

analytics = '''
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-1234567890"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-1234567890');
  </script>
</head>
'''

html_cards = []

for post in posts:
    html = template.replace('{{TITLE}}', post["title"])
    html = html.replace('{{META_TITLE}}', post["meta_title"])
    html = html.replace('{{META_DESCRIPTION}}', post["meta_desc"])
    html = html.replace('{{META_KEYWORDS}}', post["meta_kw"])
    html = html.replace('{{CANONICAL_URL}}', f'https://sqgate.online/blog/posts/{post["filename"]}')
    html = html.replace('{{AUTHOR}}', 'SQGATE Engineering')
    
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    schema_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    html = html.replace('{{DATE}}', current_date)
    html = html.replace('{{READ_TIME}}', post["read_time"])
    
    img_filename = image_files[post["filename"]]
    html = html.replace('https://sqgate.online/og-image.png', f'https://sqgate.online/blog/posts/images/{img_filename}')
    html = html.replace('</head>', analytics)
    
    schema = f'''
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{post["title"]}",
  "description": "{post["meta_desc"]}",
  "author": {{
    "@type": "Organization",
    "name": "SQGATE Engineering"
  }},
  "datePublished": "{schema_date}"
}}
'''
    html = html.replace('{{SCHEMA_JSON}}', schema)
    
    content = f'<img src="images/{img_filename}" alt="{post["title"]}">' + post["content"]
    html = html.replace('{{CONTENT}}', content)
    
    out_path = os.path.join(posts_dir, post["filename"])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    html_cards.append(f'''
    <a href="/blog/posts/{post["filename"]}" class="card">
      <div class="card-img-container">
        <img src="/blog/posts/images/{img_filename}" alt="{post["title"]}" class="card-img">
      </div>
      <div class="card-content">
        <span class="card-tag">Logic Design Series</span>
        <h2 class="card-title">{post["title"]}</h2>
        <p class="card-desc">{post["meta_desc"]}</p>
        <div class="card-meta">
          <span>{current_date}</span>
          <span>{post["read_time"]}</span>
        </div>
      </div>
    </a>''')

# Update blog/index.html
index_path = os.path.join(blog_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Insert cards right after <!-- Advanced Hardware Architectures Series --> or at the top of the grid
marker = '  <main class="grid" id="blog-grid">'
if marker in index_html:
    parts = index_html.split(marker)
    new_index = parts[0] + marker + "\\n" + "\\n".join(html_cards) + parts[1]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index)

print("All 10 posts generated successfully!")
