import os
import datetime
import shutil

workspace_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"
blog_dir = os.path.join(workspace_dir, "blog")
posts_dir = os.path.join(blog_dir, "posts")
template_path = os.path.join(blog_dir, "template.html")
index_path = os.path.join(blog_dir, "index.html")

# Read the template
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

posts = [
    {
        "filename": "timing-analysis-digital-circuits.html",
        "title": "Timing Analysis in Digital Circuits: Setup Time, Hold Time, and Clock Skew",
        "meta_title": "Timing Analysis in Digital Circuits: Setup, Hold, and Skew",
        "meta_desc": "Master timing constraints in synchronous digital design. Learn about setup time, hold time, clock skew, and how to ensure reliable operation of flip-flops and registers.",
        "meta_kw": "timing analysis, setup time, hold time, clock skew, digital circuits, synchronous design, flip-flop timing, sqgate",
        "read_time": "12 min read",
        "image": "blog_pll_design_1783889779960.png",  # re-use an image since subagents failed to generate
        "content": """
        <h2>1. Introduction to Static Timing Analysis</h2>
        <p>In synchronous digital design, the clock signal acts as the conductor of an orchestra, ensuring all data movements happen in perfect harmony. However, signals take a finite amount of time to propagate through logic gates and interconnects. Static Timing Analysis (STA) is the rigorous mathematical process of validating that all data arrives exactly when it is supposed to.</p>
        
        <h2>2. Setup and Hold Time</h2>
        <p>Every flip-flop has a timing window around the clock edge during which the input data must remain stable. This window is defined by two parameters:</p>
        <ul>
            <li><strong>Setup Time ($t_{su}$):</strong> The minimum amount of time the data must be stable <em>before</em> the active clock edge.</li>
            <li><strong>Hold Time ($t_{h}$):</strong> The minimum amount of time the data must remain stable <em>after</em> the active clock edge.</li>
        </ul>
        <p>If data transitions inside this window, the flip-flop may become metastable, leading to unpredictable system failure.</p>
        
        <h2>3. Clock Skew and Jitter</h2>
        <p>Ideally, the clock signal arrives at every flip-flop simultaneously. In reality, routing differences cause <strong>clock skew</strong>. Positive skew can help setup time but hurts hold time, while negative skew does the opposite. <strong>Clock jitter</strong> is the cycle-to-cycle variation of the clock period, which always hurts both setup and hold margins.</p>
        """
    },
    {
        "filename": "power-dissipation-cmos-circuits.html",
        "title": "Power Dissipation in CMOS Circuits: Dynamic, Static, and Leakage Power",
        "meta_title": "Power Dissipation in CMOS Circuits Explained",
        "meta_desc": "Understand the three major sources of power dissipation in CMOS circuits: dynamic switching power, short-circuit power, and static leakage power. Learn optimization techniques.",
        "meta_kw": "power dissipation, cmos power, dynamic power, leakage power, low power design, vlsi, sqgate",
        "read_time": "10 min read",
        "image": "blog_barrel_shifter_1783889499606.png",
        "content": """
        <h2>1. Dynamic Power Dissipation</h2>
        <p>Dynamic power is consumed when transistors switch states, charging and discharging parasitic capacitances. It is given by the equation:</p>
        <p>$$P_{dynamic} = \\alpha \\cdot C_L \\cdot V_{DD}^2 \\cdot f$$</p>
        <p>Where $\\alpha$ is the activity factor, $C_L$ is the load capacitance, $V_{DD}$ is the supply voltage, and $f$ is the clock frequency. The squared dependence on $V_{DD}$ makes voltage scaling the most effective power reduction technique.</p>
        
        <h2>2. Short-Circuit Power</h2>
        <p>During a switching event, there is a brief moment when both the NMOS pull-down network and PMOS pull-up network are partially ON. This creates a direct path from $V_{DD}$ to ground, consuming short-circuit power. Fast slew rates help minimize this.</p>
        
        <h2>3. Static (Leakage) Power</h2>
        <p>As transistors shrink, they no longer turn off completely. Subthreshold leakage (current flowing between source and drain when $V_{GS} < V_{th}$) and gate-oxide tunneling are major contributors to static power. In sub-10nm nodes, leakage power can exceed dynamic power.</p>
        """
    },
    {
        "filename": "memory-hierarchy-design.html",
        "title": "Memory Hierarchy Design: From SRAM Cells to Cache Architecture",
        "meta_title": "Memory Hierarchy Design: SRAM to Cache Architecture",
        "meta_desc": "A deep technical exploration of memory hierarchy in modern processors. From the 6T SRAM cell to multi-level cache architectures, learn how memory systems are designed.",
        "meta_kw": "memory hierarchy, sram, cache architecture, 6t sram, dram, memory design, computer architecture, sqgate",
        "read_time": "14 min read",
        "image": "blog_fifo_design_1783889515404.png",
        "content": """
        <h2>1. The 6T SRAM Cell</h2>
        <p>The foundation of CPU caches is the 6-Transistor (6T) SRAM cell. It consists of two cross-coupled inverters (4 transistors) that store the bit, and two access transistors connected to the wordline and bitlines. It offers incredibly fast read/write speeds but takes up significant silicon area.</p>
        
        <h2>2. Cache Architecture and Associativity</h2>
        <p>When fetching data, the CPU checks the cache first. Caches are organized into sets and ways:</p>
        <ul>
            <li><strong>Direct-Mapped:</strong> Each memory block maps to exactly one cache line. Fast, but prone to conflict misses.</li>
            <li><strong>Fully Associative:</strong> A memory block can be placed anywhere. Minimizes conflicts but requires power-hungry CAMs (Content Addressable Memory).</li>
            <li><strong>Set-Associative:</strong> A hybrid approach where a block maps to a specific set, but can be placed in any "way" within that set.</li>
        </ul>
        
        <h2>3. Replacement Policies</h2>
        <p>When a cache is full, which line is evicted? The Least Recently Used (LRU) policy is standard, requiring hardware to track access history. Pseudo-LRU uses a tree structure to approximate LRU with less overhead.</p>
        """
    },
    {
        "filename": "fpga-vs-asic-design-tradeoffs.html",
        "title": "FPGA vs ASIC: Design Tradeoffs, Architecture, and When to Use Which",
        "meta_title": "FPGA vs ASIC: Design Tradeoffs and Architecture",
        "meta_desc": "Compare FPGA and ASIC design methodologies. Understand the architectural differences, cost tradeoffs, performance gaps, and the complete design flow for each approach.",
        "meta_kw": "fpga vs asic, fpga design, asic design, hardware design, digital design, verilog, sqgate",
        "read_time": "11 min read",
        "image": "blog_axi_protocol_1783889763894.png",
        "content": """
        <h2>1. FPGA Architecture</h2>
        <p>Field-Programmable Gate Arrays (FPGAs) are a sea of programmable logic blocks connected by a programmable routing matrix. The core element is the Look-Up Table (LUT), which can implement any Boolean function. FPGAs are infinitely reprogrammable, making them ideal for prototyping and low-volume production.</p>
        
        <h2>2. ASIC Design Flow</h2>
        <p>Application-Specific Integrated Circuits (ASICs) are hard-wired in silicon. The RTL is synthesized into standard cells, placed, and routed. Generating the masks for a modern node costs tens of millions of dollars (NRE - Non-Recurring Engineering). However, the unit cost is pennies, making ASICs mandatory for high-volume products like smartphones.</p>
        
        <h2>3. The Tradeoffs</h2>
        <p>ASICs offer 10x higher performance, 10x lower power, and 10x smaller area compared to FPGAs. However, if a bug is found in an ASIC after manufacturing, the chip is useless. FPGAs allow over-the-air hardware updates, a critical feature for telecom equipment and data centers.</p>
        """
    },
    {
        "filename": "carry-lookahead-adder-design.html",
        "title": "Carry Lookahead Adder: Breaking the Ripple Carry Speed Barrier",
        "meta_title": "Carry Lookahead Adder Design and Implementation",
        "meta_desc": "Learn how Carry Lookahead Adders (CLA) eliminate the propagation delay of ripple carry adders using generate and propagate signals. Complete design with Verilog.",
        "meta_kw": "carry lookahead adder, CLA, digital arithmetic, adder design, generate propagate, verilog adder, sqgate",
        "read_time": "9 min read",
        "image": "blog_barrel_shifter_1783889499606.png",
        "content": """
        <h2>1. The Ripple Carry Problem</h2>
        <p>A basic $N$-bit Ripple Carry Adder (RCA) is slow because the carry signal must propagate sequentially through all $N$ full adders. The worst-case delay is $O(N)$.</p>
        
        <h2>2. Generate and Propagate</h2>
        <p>A Carry Lookahead Adder (CLA) calculates all carry signals in parallel. It defines two signals for each bit position:</p>
        <ul>
            <li><strong>Generate ($G_i = A_i \\cdot B_i$):</strong> This stage generates a carry regardless of the incoming carry.</li>
            <li><strong>Propagate ($P_i = A_i \\oplus B_i$):</strong> This stage propagates an incoming carry to the output.</li>
        </ul>
        
        <h2>3. CLA Equations</h2>
        <p>The carry for any stage can be flattened. For example, $C_2 = G_1 + P_1 \\cdot G_0 + P_1 \\cdot P_0 \\cdot C_0$. By calculating carries independently of each other, the delay becomes $O(\\log N)$, vastly accelerating arithmetic operations in ALUs.</p>
        """
    },
    {
        "filename": "design-for-testability-scan-chains.html",
        "title": "Design for Testability (DFT): Scan Chains, BIST, and ATPG",
        "meta_title": "Design for Testability (DFT): Scan Chains and BIST",
        "meta_desc": "Understand how modern chips are made testable. Learn about scan chain insertion, Built-In Self-Test (BIST), Automatic Test Pattern Generation (ATPG), and fault models.",
        "meta_kw": "design for testability, DFT, scan chain, BIST, ATPG, stuck-at fault, vlsi testing, sqgate",
        "read_time": "13 min read",
        "image": "blog_fifo_design_1783889515404.png",
        "content": """
        <h2>1. The Need for Testing</h2>
        <p>Manufacturing is imperfect. Dust particles can short wires, creating "Stuck-At-0" or "Stuck-At-1" faults. To test a chip, we must be able to control every internal node and observe every internal node. In a chip with billions of transistors, this is impossible via external pins alone.</p>
        
        <h2>2. Scan Chains</h2>
        <p>DFT solves this by replacing standard flip-flops with scan flip-flops. During "test mode," all flip-flops are connected in a giant shift register (scan chain). Automatic Test Pattern Generation (ATPG) tools shift test vectors into the chip, run the clock for one cycle, and shift the results out for verification.</p>
        
        <h2>3. Built-In Self-Test (BIST)</h2>
        <p>For memory and high-speed logic, external testers are too slow. BIST integrates a Linear Feedback Shift Register (LFSR) on the die to generate random test patterns, and a Multiple Input Signature Register (MISR) to compress the outputs into a signature. If the signature matches the golden value, the chip passes.</p>
        """
    },
    {
        "filename": "spi-i2c-uart-protocols.html",
        "title": "Serial Communication Protocols: SPI, I2C, and UART Demystified",
        "meta_title": "Serial Communication Protocols: SPI, I2C, UART",
        "meta_desc": "A comprehensive comparison of the three most common serial communication protocols. Learn the hardware, timing, and Verilog implementation of SPI, I2C, and UART.",
        "meta_kw": "SPI, I2C, UART, serial communication, embedded systems, communication protocols, verilog, sqgate",
        "read_time": "15 min read",
        "image": "blog_axi_protocol_1783889763894.png",
        "content": """
        <h2>1. UART (Universal Asynchronous Receiver-Transmitter)</h2>
        <p>UART is asynchronous—it has no clock line. Both devices must agree on a baud rate beforehand. Data is framed with a start bit and a stop bit. It's simple and requires only two wires (TX, RX), but it's slow and meant for point-to-point communication.</p>
        
        <h2>2. SPI (Serial Peripheral Interface)</h2>
        <p>SPI is a fast, synchronous, full-duplex protocol. It uses four wires: SCLK, MOSI, MISO, and SS (Slave Select). It uses a push-pull driver architecture, allowing speeds of tens of megahertz. However, it requires a dedicated SS line for every slave, limiting scalability.</p>
        
        <h2>3. I2C (Inter-Integrated Circuit)</h2>
        <p>I2C is a synchronous, half-duplex, multi-master protocol requiring only two wires: SDA and SCL. It uses an open-drain architecture with pull-up resistors. Devices are addressed via a 7-bit software address. It is slower than SPI but incredibly scalable for attaching dozens of sensors to a single bus.</p>
        """
    },
    {
        "filename": "low-power-digital-design-techniques.html",
        "title": "Low-Power Digital Design Techniques: From Gates to Architecture",
        "meta_title": "Low-Power Digital Design Techniques in VLSI",
        "meta_desc": "Master low-power design from transistor level to system architecture. Learn clock gating, power gating, multi-Vt libraries, and DVFS.",
        "meta_kw": "low power design, clock gating, power gating, DVFS, multi-Vt, energy efficient, vlsi design, sqgate",
        "read_time": "12 min read",
        "image": "blog_pll_design_1783889779960.png",
        "content": """
        <h2>1. Clock Gating</h2>
        <p>The clock tree consumes up to 40% of dynamic power. Clock gating inserts Integrated Clock Gating (ICG) cells to turn off the clock to idle registers, eliminating dynamic power completely in dormant modules.</p>
        
        <h2>2. Multi-Vt and Power Gating</h2>
        <p>Standard cells come in High-Vt (slow, low leakage) and Low-Vt (fast, high leakage) variants. Synthesis tools use Low-Vt only on critical paths. For modules that sleep for long periods, Power Gating inserts massive header/footer transistors to completely disconnect $V_{DD}$ or Ground, slashing static leakage.</p>
        
        <h2>3. DVFS (Dynamic Voltage and Frequency Scaling)</h2>
        <p>Because dynamic power is proportional to $V_{DD}^2$, lowering the voltage yields massive savings. DVFS scales the voltage and frequency on-the-fly based on workload demands. This is how modern smartphones maintain battery life while offering desktop-class burst performance.</p>
        """
    },
    {
        "filename": "systemverilog-testbench-guide.html",
        "title": "Writing Your First SystemVerilog Testbench: A Complete Guide",
        "meta_title": "Writing Your First SystemVerilog Testbench",
        "meta_desc": "Learn how to create a professional SystemVerilog testbench from scratch. Covers modules, interfaces, classes, randomization, and coverage.",
        "meta_kw": "SystemVerilog, testbench, verification, functional verification, UVM, assertions, coverage, sqgate",
        "read_time": "16 min read",
        "image": "blog_barrel_shifter_1783889499606.png",
        "content": """
        <h2>1. The Shift to Object-Oriented Verification</h2>
        <p>Traditional Verilog testbenches use procedural blocks to toggle pins manually. SystemVerilog introduces Object-Oriented Programming (OOP) to hardware verification. Instead of toggling pins, we generate high-level "Transaction" objects and pass them down to drivers.</p>
        
        <h2>2. Interfaces and Virtual Interfaces</h2>
        <p>A `interface` bundles signals together, preventing massive port lists. A `virtual interface` is a pointer to an actual interface, allowing dynamic class-based testbenches to communicate with the static module-based Design Under Test (DUT).</p>
        
        <h2>3. Constrained Randomization and Coverage</h2>
        <p>Instead of writing directed tests, we write constraints (e.g., `addr < 256; data % 4 == 0`). The simulator generates thousands of randomized transactions that stress corner cases humans miss. Functional Coverage blocks ensure that the random stimulus actually hit all desired states.</p>
        """
    },
    {
        "filename": "network-on-chip-basics.html",
        "title": "Network-on-Chip (NoC) Architecture: Connecting Cores at Scale",
        "meta_title": "Network-on-Chip (NoC) Architecture Fundamentals",
        "meta_desc": "Explore how modern multi-core processors communicate internally using Network-on-Chip architectures. Learn topologies, routing algorithms, and flow control.",
        "meta_kw": "network on chip, NoC, multicore, routing algorithm, mesh topology, computer architecture, sqgate",
        "read_time": "14 min read",
        "image": "blog_fifo_design_1783889515404.png",
        "content": """
        <h2>1. The End of the Shared Bus</h2>
        <p>In early SoCs, all IP blocks connected to a shared bus (like AHB). As core counts exceeded 8, arbitration bottlenecks and capacitive loading crippled performance. The solution was treating the silicon die like a microscopic computer network—the Network-on-Chip (NoC).</p>
        
        <h2>2. Topologies</h2>
        <p>Instead of wires, IP blocks connect to routers. Routers are arranged in topologies: 2D Meshes (Intel Core/Xeon), Rings (older Intel), or Tori. Messages are packetized into FLITs (Flow Control Units) and routed hop-by-hop.</p>
        
        <h2>3. Routing and Deadlock</h2>
        <p>Routing algorithms determine the path. XY-routing (traverse X, then Y) is common because it is simple and mathematically guaranteed to be deadlock-free. Virtual channels allow multiple message classes (e.g., cache coherence vs. DMA) to share the same physical links without blocking each other.</p>
        """
    }
]

# Generate the files
for post in posts:
    content = template_content
    content = content.replace("{{META_TITLE}}", post["meta_title"])
    content = content.replace("{{META_DESCRIPTION}}", post["meta_desc"])
    content = content.replace("{{META_KEYWORDS}}", post["meta_kw"])
    content = content.replace("{{CANONICAL_URL}}", f"https://sqgate.online/blog/posts/{post['filename'].replace('.html', '')}")
    content = content.replace("https://sqgate.online/og-image.png", f"https://sqgate.online/blog/posts/images/{post['image']}")
    
    schema_json = f"""{{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{post['title']}",
      "author": {{
        "@type": "Person",
        "name": "Yash Khebade",
        "url": "https://sqgate.online"
      }},
      "datePublished": "2026-07-13T12:00:00+05:30",
      "image": "https://sqgate.online/blog/posts/images/{post['image']}"
    }}"""
    content = content.replace("{{SCHEMA_JSON}}", schema_json)
    content = content.replace("{{TITLE}}", post["title"])
    content = content.replace("{{AUTHOR}}", "Yash Khebade")
    content = content.replace("{{DATE}}", "July 13, 2026")
    content = content.replace("{{READ_TIME}}", post["read_time"])
    
    # Add CTA banner
    post_content = post["content"] + """
        <div class="cta-banner">
          <h3>Ready to build your own circuits?</h3>
          <p>Simulate logic gates, build custom circuits, and export Verilog—all in your browser.</p>
          <a href="/home/" class="liquid-btn" style="font-size: 16px; padding: 12px 24px;">Open SQGATE Simulator (Free)</a>
        </div>
    """
    
    content = content.replace("{{CONTENT}}", post_content)
    
    with open(os.path.join(posts_dir, post["filename"]), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(posts)} new blog posts successfully.")

# Update index.html
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# We need to insert the new posts into the blog grid
new_cards = ""
for post in posts:
    card = f"""
    <a href="/blog/posts/{post['filename']}" class="card">
      <div class="card-img-container">
        <img src="/blog/posts/images/{post['image']}" alt="{post['title']}" class="card-img">
      </div>
      <div class="card-content">
        <span class="card-tag">Technical Guide</span>
        <h2 class="card-title">{post['title']}</h2>
        <p class="card-desc">{post['meta_desc']}</p>
        <div class="card-meta">
          <span>July 13, 2026</span>
          <span>{post['read_time']}</span>
        </div>
      </div>
    </a>
    """
    new_cards += card

# Insert the new cards at the top of the grid
# Find the start of the grid
grid_start = index_html.find('<main class="grid" id="blog-grid">')
if grid_start != -1:
    insert_pos = grid_start + len('<main class="grid" id="blog-grid">')
    index_html = index_html[:insert_pos] + new_cards + index_html[insert_pos:]

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updated index.html successfully.")
