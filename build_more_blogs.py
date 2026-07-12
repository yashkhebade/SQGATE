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
    "evolution-of-digital-logic.html": "blog_evolution_logic_1783146066493.png",
    "decoders-encoders-guide.html": "blog_decoders_encoders_1783146077950.png",
    "demultiplexers-explained.html": "blog_demultiplexers_1783146088471.png",
    "ring-johnson-counters.html": "blog_ring_johnson_counters_1783146098212.png",
    "hazards-glitches-logic.html": "blog_hazards_glitches_1783146108842.png",
    "metastability-digital-systems.html": "blog_metastability_1783146127228.png",
    "setup-hold-time-violations.html": "blog_setup_hold_time_1783146137976.png",
    "designing-4bit-cpu.html": "blog_designing_4bit_cpu_1783146148827.png",
    "verilog-vs-vhdl-guide.html": "blog_verilog_vs_vhdl_1783146159597.png",
    "intro-systemverilog-verification.html": "blog_systemverilog_1783146169199.png",
}

for dest, src in image_files.items():
    src_path = os.path.join(artifact_dir, src)
    if os.path.exists(src_path):
        shutil.copy(src_path, os.path.join(images_dir, src))

posts = [
    {
        "filename": "evolution-of-digital-logic.html",
        "title": "The Evolution of Digital Logic: From Relays to Silicon",
        "meta_title": "Evolution of Digital Logic: Relays to Silicon processors",
        "meta_desc": "Explore the history of computing hardware. Learn how logic gates evolved from mechanical relays and vacuum tubes to modern silicon transistors.",
        "meta_kw": "digital logic history, vacuum tubes, relays, silicon transistors, computer history",
        "read_time": "8 min read",
        "content": """
<h2>In the Beginning: Mechanical Relays</h2>
<p>Before the invention of the microchip, computers were massive, loud, and incredibly slow. Early electromechanical computers, like the Harvard Mark I, used mechanical relays to perform logic operations. A relay is essentially an electrically operated switch. While functional, they were physically large, consumed massive amounts of power, and suffered from mechanical wear and tear, limiting computing speed to mere hertz.</p>
<h2>The Vacuum Tube Era</h2>
<p>The next major leap was the vacuum tube, which eliminated moving parts entirely. By controlling the flow of electrons in a vacuum, these tubes could switch thousands of times faster than relays. ENIAC, one of the first general-purpose electronic computers, used nearly 18,000 vacuum tubes. However, they were notorious for generating immense heat and burning out frequently, making maintenance a daily nightmare.</p>
<h2>The Transistor Revolution</h2>
<p>In 1947, scientists at Bell Labs invented the transistor. Made from semiconductor materials like germanium and later silicon, the transistor could perform the same switching function as a vacuum tube but was a fraction of the size, generated almost no heat, and was vastly more reliable. This marked the birth of modern solid-state electronics and paved the way for the integrated circuit (IC), eventually leading to modern CPUs packing billions of transistors into a single chip.</p>
"""
    },
    {
        "filename": "decoders-encoders-guide.html",
        "title": "Decoders and Encoders: Understanding Data Conversion",
        "meta_title": "Digital Decoders and Encoders Explained | Logic Design",
        "meta_desc": "A comprehensive guide to digital decoders and encoders. Learn how to convert binary data into specific output lines and vice versa in digital circuits.",
        "meta_kw": "digital decoder, binary encoder, priority encoder, combinational logic, logic design",
        "read_time": "7 min read",
        "content": """
<h2>What is a Decoder?</h2>
<p>A decoder is a combinational logic circuit that converts binary information from N input lines to a maximum of 2^N unique output lines. If the N-bit binary input has a value of 'K', the decoder will activate (set to logic 1) exactly the K-th output line, keeping all other output lines at logic 0.</p>
<p>Decoders are heavily used in memory systems (to select specific memory addresses based on a binary address bus) and in CPU instruction decoding (to activate the correct internal CPU pathways based on the opcode of an instruction).</p>
<h2>What is an Encoder?</h2>
<p>An encoder performs the exact opposite function of a decoder. It has 2^N input lines and N output lines. It generates the binary code corresponding to the input value that is active. For example, in an 8-to-3 encoder, if input line 5 is High, the output will be the binary representation of 5 (101).</p>
<h2>The Priority Encoder</h2>
<p>A standard encoder has a fatal flaw: what happens if multiple input lines are High simultaneously? The output becomes garbage. To solve this, we use a Priority Encoder. It assigns priority to the input lines. If multiple inputs are High, the encoder outputs the binary code of the input line with the highest priority (usually the one with the highest index), ignoring all others. Priority encoders are critical in handling CPU interrupts.</p>
"""
    },
    {
        "filename": "demultiplexers-explained.html",
        "title": "Demultiplexers (DEMUX): The Opposite of MUX",
        "meta_title": "Demultiplexers (DEMUX) Explained in Digital Logic",
        "meta_desc": "Learn how Demultiplexers (DEMUX) take a single input signal and route it to multiple output channels using select lines.",
        "meta_kw": "demultiplexer, DEMUX, data routing, digital logic, combinational circuit",
        "read_time": "6 min read",
        "content": """
<h2>The Role of a DEMUX</h2>
<p>In a previous article, we explored the Multiplexer (MUX), which acts as a digital switch combining multiple inputs into a single output. A Demultiplexer (DEMUX) is the exact reverse. It takes a single input data line and routes it to any one of several output lines.</p>
<h2>How it Works</h2>
<p>A 1-to-4 DEMUX has 1 data input, 4 data outputs, and 2 select lines. Based on the binary value of the select lines (00, 01, 10, or 11), the input data is connected directly to the corresponding output line. The other three output lines remain at logic 0.</p>
<h2>Decoders vs. Demultiplexers</h2>
<p>If you look at the logic gate diagram of a DEMUX, you will notice it is nearly identical to a Decoder! The only difference is how we use the pins. If you take a standard 2-to-4 Decoder with an "Enable" pin, you can use the Enable pin as your data input, and the address pins as your select lines. Just like that, your Decoder has become a DEMUX!</p>
"""
    },
    {
        "filename": "ring-johnson-counters.html",
        "title": "Understanding Ring Counters and Johnson Counters",
        "meta_title": "Ring Counters and Johnson Counters | Sequential Logic",
        "meta_desc": "Discover how to build specialized counters using shift registers. A deep dive into the architecture and applications of Ring and Johnson counters.",
        "meta_kw": "ring counter, johnson counter, shift register, sequential logic, digital counters",
        "read_time": "8 min read",
        "content": """
<h2>Shift Register Based Counters</h2>
<p>While traditional binary counters count in a standard binary sequence (000, 001, 010...), there are situations where we want a different sequence, such as a single active bit shifting across outputs. We can achieve this by taking a standard shift register and feeding its output back into its input.</p>
<h2>The Ring Counter</h2>
<p>A Ring Counter is created by connecting the output of the last flip-flop in a shift register directly back to the D-input of the first flip-flop. To initialize it, one flip-flop is preset to 1, while the rest are cleared to 0. With each clock pulse, that single '1' circulates around the ring indefinitely.</p>
<p>A 4-bit ring counter has 4 states (1000, 0100, 0010, 0001) and requires no decoding gates, making it extremely fast and perfect for controlling stepper motors or sequential logic state machines.</p>
<h2>The Johnson Counter</h2>
<p>A Johnson Counter (also called a Twisted Ring Counter) is very similar, but instead of feeding the standard output (Q) back to the input, it feeds the inverted output (NOT Q) of the last flip-flop back to the first. Starting from 0000, it fills with 1s (1000, 1100, 1110, 1111) and then empties (0111, 0011, 0001, 0000).</p>
<p>The primary advantage of a Johnson counter is that an N-bit Johnson counter provides 2N states, doubling the number of states compared to a standard Ring Counter using the same number of flip-flops.</p>
"""
    },
    {
        "filename": "hazards-glitches-logic.html",
        "title": "Hazards and Glitches in Combinational Circuits",
        "meta_title": "Digital Logic Hazards & Glitches | How to Fix Them",
        "meta_desc": "Understand the causes of static and dynamic hazards in combinational logic circuits and learn how to eliminate them using K-Maps and redundant logic.",
        "meta_kw": "digital hazard, logic glitch, static hazard, dynamic hazard, combinational logic",
        "read_time": "9 min read",
        "content": """
<h2>The Reality of Propagation Delay</h2>
<p>In pure boolean algebra, when an input changes, the output evaluates instantaneously. In the real world, logic gates are physical devices built from transistors, and it takes a tiny fraction of a nanosecond for a voltage change to propagate through them. This propagation delay is the root cause of digital hazards.</p>
<h2>Static Hazards</h2>
<p>A static hazard occurs when a single input variable changes, and the output is supposed to remain constant (e.g., stay at 1), but momentarily drops to 0 before returning to 1. This momentary spike is called a glitch. If this glitch feeds into the clock pin of a flip-flop, it can cause catastrophic unintended state changes in your circuit.</p>
<h2>Fixing Hazards with K-Maps</h2>
<p>Hazards occur when a signal takes two different paths through a circuit with slightly different propagation delays. In a Karnaugh Map, a static hazard exists if there are two adjacent 1s that are grouped in separate groups, but not grouped together.</p>
<p>To eliminate the hazard, we add redundant logic. We add an extra grouping in the K-Map that covers the adjacent 1s that bridge the original groups. This extra logic gate ensures that even if one path is delayed, the redundant path maintains the output stability during the transition.</p>
"""
    },
    {
        "filename": "metastability-digital-systems.html",
        "title": "Metastability in Digital Systems: Causes and Cures",
        "meta_title": "Understanding Metastability in Digital Circuits | SQGATE",
        "meta_desc": "Explore the dangerous phenomenon of metastability in digital electronics. Learn why it happens and how synchronizers can protect your circuits.",
        "meta_kw": "metastability, flip-flop, digital systems, synchronizer, clock domain crossing, CDC",
        "read_time": "8 min read",
        "content": """
<h2>The Forbidden State</h2>
<p>We are taught that digital signals are strictly binary: either a clean 0 or a clean 1. However, if a flip-flop's input changes at the exact moment the clock edge triggers, the flip-flop can enter a bizarre, unstable state known as metastability. In this state, the output voltage hovers halfway between a 0 and a 1.</p>
<h2>The Danger of Metastability</h2>
<p>A metastable signal is catastrophic. It is neither 0 nor 1, meaning downstream logic gates might interpret it differently. One gate might see it as a 1, while another sees it as a 0, completely breaking the logic of your circuit. Furthermore, the time it takes for a metastable flip-flop to randomly resolve back to a stable 0 or 1 is theoretically unbounded.</p>
<h2>The Cure: Synchronizers</h2>
<p>Metastability cannot be entirely prevented when dealing with asynchronous inputs (like a button press from a human, or data from a different clock domain). However, we can isolate it.</p>
<p>The standard cure is a multi-stage synchronizer: placing two or three flip-flops in series. The first flip-flop catches the asynchronous signal and may go metastable. However, we give it a full clock cycle to resolve its metastability before the second flip-flop samples its output. By the time the signal reaches the rest of the circuit, the probability of it still being metastable is astronomically low.</p>
"""
    },
    {
        "filename": "setup-hold-time-violations.html",
        "title": "Setup and Hold Time Violations Explained",
        "meta_title": "Setup and Hold Time Violations | Digital Timing Analysis",
        "meta_desc": "Master digital timing analysis. Understand flip-flop setup time, hold time, and how clock skew can lead to devastating timing violations.",
        "meta_kw": "setup time, hold time, timing violation, clock skew, static timing analysis",
        "read_time": "9 min read",
        "content": """
<h2>The Critical Timing Window</h2>
<p>For a flip-flop to reliably sample incoming data on a clock edge, the data cannot be changing at the exact moment the clock transitions. There is a strict window of time around the clock edge where the data must remain absolutely stable.</p>
<h2>Setup Time (t_setup)</h2>
<p>Setup time is the minimum amount of time the data signal must be stable <strong>before</strong> the active clock edge arrives. If the data changes too late (violating the setup time), the flip-flop may capture the old value, or worse, enter metastability. Setup time violations usually occur when the combinational logic between two flip-flops is too complex, causing the signal to arrive too late.</p>
<h2>Hold Time (t_hold)</h2>
<p>Hold time is the minimum amount of time the data signal must remain stable <strong>after</strong> the active clock edge has passed. If the data changes too quickly after the clock edge (violating the hold time), the flip-flop may capture the new value instead of the intended one. Hold time violations often happen due to "clock skew" where the clock signal reaches the receiving flip-flop slightly later than the transmitting flip-flop.</p>
<h2>Fixing Violations</h2>
<p>Fixing a setup violation usually requires slowing down the clock frequency or simplifying the combinational logic. Fixing a hold violation involves adding artificial delay (like buffer gates) to the data path so the signal doesn't arrive too quickly.</p>
"""
    },
    {
        "filename": "designing-4bit-cpu.html",
        "title": "Designing a Simple 4-Bit CPU from Scratch",
        "meta_title": "How to Design a 4-Bit CPU from Scratch | Architecture",
        "meta_desc": "A conceptual walkthrough of building a minimal 4-bit processor. Learn how the ALU, Registers, and Control Unit interact to execute instructions.",
        "meta_kw": "4-bit CPU, CPU design, computer architecture, control unit, ALU, registers",
        "read_time": "10 min read",
        "content": """
<h2>The Anatomy of a CPU</h2>
<p>Designing a Central Processing Unit (CPU) seems like magic, but it boils down to orchestrating three main components: The Registers (temporary storage), the Arithmetic Logic Unit (the calculator), and the Control Unit (the brain orchestrating the flow).</p>
<h2>The Datapath</h2>
<p>In a simple 4-bit CPU, our datapath revolves around a central 4-bit bus. We might have two general-purpose registers (A and B). The ALU takes inputs from these registers and outputs the result back onto the bus. Crucially, every component connected to the bus must use Tri-State Buffers, ensuring only one component is allowed to "talk" on the bus at any given microsecond.</p>
<h2>The Instruction Cycle: Fetch, Decode, Execute</h2>
<p>The CPU operates in a relentless loop:</p>
<ol>
    <li><strong>Fetch:</strong> The Program Counter (PC) outputs an address to the ROM. The ROM outputs the 4-bit instruction at that address, which is latched into the Instruction Register (IR).</li>
    <li><strong>Decode:</strong> The Control Unit looks at the 4-bit instruction in the IR and determines what needs to happen.</li>
    <li><strong>Execute:</strong> The Control Unit asserts specific control signals. For example, if the instruction is "ADD", it asserts the signals to output Register A, output Register B into the ALU, set the ALU to addition mode, and latch the result into a target register.</li>
</ol>
<p>By defining a simple instruction set and wiring a Control Unit (using an FSM or microcode ROM) to assert the correct control lines for each instruction, you breathe life into the silicon.</p>
"""
    },
    {
        "filename": "verilog-vs-vhdl-guide.html",
        "title": "Verilog vs VHDL: Which Should You Learn First?",
        "meta_title": "Verilog vs VHDL: A Guide for Digital Designers | SQGATE",
        "meta_desc": "Comparing Verilog and VHDL. Understand the pros and cons of the two dominant Hardware Description Languages used in FPGA and ASIC design.",
        "meta_kw": "Verilog, VHDL, HDL, hardware description language, FPGA programming",
        "read_time": "8 min read",
        "content": """
<h2>The Language of Hardware</h2>
<p>When designing modern digital circuits for FPGAs or ASICs, you don't draw schematics. You write code using a Hardware Description Language (HDL). The two industry heavyweights are Verilog and VHDL. While they achieve the same goal, their philosophies are entirely different.</p>
<h2>VHDL: The Strictly Typed Veteran</h2>
<p>VHDL (VHSIC Hardware Description Language) is heavily inspired by the Ada programming language. It is strongly typed and highly verbose. You must explicitly declare everything, and type conversions are strict. <br>
<strong>Pros:</strong> Excellent for massive, safety-critical aerospace or military projects. If your VHDL code compiles without errors, there's a very high chance it accurately represents the hardware you intended.<br>
<strong>Cons:</strong> The learning curve is steep, and it takes significantly more lines of code to express simple concepts.</p>
<h2>Verilog: The C-Like Alternative</h2>
<p>Verilog was designed to look and feel like the C programming language. It is loosely typed and much more concise.<br>
<strong>Pros:</strong> Much easier to learn for software engineers. You can prototype and write logic significantly faster than in VHDL.<br>
<strong>Cons:</strong> Because it is loosely typed, it is easier to write Verilog code that successfully compiles but synthesizes into unintended, buggy hardware (like accidental latches).</p>
<h2>Which to Choose?</h2>
<p>If you are a beginner looking to get your feet wet in FPGA design, <strong>Verilog is generally the recommended starting point</strong> due to its gentler learning curve and massive amount of online community support.</p>
"""
    },
    {
        "filename": "intro-systemverilog-verification.html",
        "title": "Introduction to SystemVerilog for Hardware Verification",
        "meta_title": "SystemVerilog Verification: Beyond Standard Verilog",
        "meta_desc": "Learn why SystemVerilog replaced Verilog for advanced hardware verification. Explore OOP features, constrained random testing, and coverage.",
        "meta_kw": "SystemVerilog, hardware verification, UVM, constrained random testing, testbench",
        "read_time": "9 min read",
        "content": """
<h2>The Verification Bottleneck</h2>
<p>In modern ASIC and FPGA development, writing the hardware code (RTL design) is only 30% of the effort. The other 70% is spent on verification—proving that the design actually works under all possible conditions. Traditional Verilog testbenches quickly become unmanageable spaghetti code when testing complex SoCs.</p>
<h2>Enter SystemVerilog</h2>
<p>SystemVerilog is a massive superset of Verilog. While it added a few new features for hardware design (like `always_ff` and `always_comb` to prevent accidental latches), its true power lies in its verification capabilities. SystemVerilog effectively merged a Hardware Description Language with a full-fledged Object-Oriented Programming (OOP) language like C++ or Java.</p>
<h2>Key Verification Features</h2>
<ul>
    <li><strong>Classes and OOP:</strong> You can create objects, inherit properties, and build modular, reusable testbench environments.</li>
    <li><strong>Constrained Random Testing:</strong> Instead of manually writing thousands of specific tests, you define rules (constraints), and SystemVerilog automatically generates randomized, valid test vectors to bombard your design, finding edge cases you never would have thought of.</li>
    <li><strong>Functional Coverage:</strong> SystemVerilog can track exactly which states and conditions in your hardware have been hit by the random tests, allowing you to mathematically prove when verification is "done."</li>
</ul>
<p>Today, SystemVerilog (specifically using the UVM methodology) is the absolute industry standard for professional hardware verification.</p>
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
    
    # Note: canonical URLs do NOT have .html for Cloudflare Pages
    canonical_url = f'https://sqgate.online/blog/posts/{post["filename"].replace(".html", "")}'
    html = html.replace('{{CANONICAL_URL}}', canonical_url)
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
        <span class="card-tag">Advanced Series</span>
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

# Insert cards right after <main class="grid" id="blog-grid">
marker = '  <main class="grid" id="blog-grid">'
if marker in index_html:
    parts = index_html.split(marker)
    new_index = parts[0] + marker + "\\n" + "\\n".join(html_cards) + parts[1]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index)

# Rewrite sitemap.xml to be perfect
# I will grab all .html files in the workspace and generate a correct sitemap.xml
sitemap_path = os.path.join(workspace_dir, "sitemap.xml")

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

urls = set()

for root_dir, dirs, files in os.walk(workspace_dir):
    if ".git" in root_dir or "node_modules" in root_dir or ".wrangler" in root_dir or "dist_cf" in root_dir:
        continue
    
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root_dir, file)
            rel_path = os.path.relpath(filepath, workspace_dir).replace('\\', '/')
            
            # Skip templates or partials if any
            if "template.html" in rel_path or "google" in rel_path:
                continue
                
            if rel_path == "index.html" or rel_path == "home/index.html":
                correct_url = "https://sqgate.online/"
            elif rel_path.endswith("/index.html"):
                folder_path = rel_path[:-10] # remove index.html
                correct_url = f"https://sqgate.online/{folder_path}"
            else:
                name_without_ext = rel_path[:-5]
                correct_url = f"https://sqgate.online/{name_without_ext}"
            
            if correct_url not in urls:
                urls.add(correct_url)
                
                # Determine priority
                priority = "0.6"
                if correct_url == "https://sqgate.online/":
                    priority = "1.0"
                elif "blog/posts/" in correct_url:
                    priority = "0.8"
                elif "index.html" in rel_path:
                    priority = "0.9" # Tools
                
                sitemap_xml += f'  <url>\\n'
                sitemap_xml += f'    <loc>{correct_url}</loc>\\n'
                sitemap_xml += f'    <lastmod>{current_date}</lastmod>\\n'
                sitemap_xml += f'    <changefreq>weekly</changefreq>\\n'
                sitemap_xml += f'    <priority>{priority}</priority>\\n'
                sitemap_xml += f'  </url>\\n'

sitemap_xml += '</urlset>'

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print("All 10 posts generated and sitemap.xml fully updated successfully!")
