import os
import re

base_dir = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes"

contents = {
    "k-map/index.html": """
<!-- UNIQUE TOOL CONTENT -->
<div class="tool-article" style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px; color: rgba(255,255,255,0.8); line-height: 1.7; font-family: var(--font-sans);">
  <h2 style="color: #fff; font-size: 24px; margin-bottom: 16px;">What is a Karnaugh Map?</h2>
  <p style="margin-bottom: 16px;">A Karnaugh Map (or K-map) is a visual method used to simplify Boolean algebra expressions. Instead of relying on complex algebraic theorems, a K-map organizes truth table variables into a grid where cells differing by only one variable are adjacent (using Gray code). This allows engineers to easily spot patterns and group ones together to find the simplest possible Sum of Products (SOP) or Product of Sums (POS) expression.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">How to Use the SQGate K-Map Solver</h3>
  <p style="margin-bottom: 16px;">Our interactive solver supports up to 6 variables. To begin, select your desired variable count from the top control bar (e.g., 4 Variables for ABCD). The grid will automatically adjust. Simply click on the cells to toggle their states between 0, 1, and X (Don't Care). As you input your minterms, the engine will instantly highlight the optimal prime implicant groupings on the grid and display the simplified Boolean expression in real-time. For 5 and 6 variable K-maps, the interface splits into multiple 4x4 planes to represent the higher dimensions.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">Worked Example: 4-Variable Simplification</h3>
  <p style="margin-bottom: 16px;">Imagine you have a truth table for variables A, B, C, D where the output is 1 for minterms m(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14). By clicking these cells on the K-map to turn them green (1), the solver will group the corners and edges to yield the simplified SOP expression: <code>C' + A'D' + BD'</code>. You can then click the "Copy Verilog assign" button to instantly drop this logic into your HDL code.</p>
</div>
""",
    "fsm/index.html": """
<!-- UNIQUE TOOL CONTENT -->
<div class="tool-article" style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px; color: rgba(255,255,255,0.8); line-height: 1.7; font-family: var(--font-sans);">
  <h2 style="color: #fff; font-size: 24px; margin-bottom: 16px;">What is a Finite State Machine (FSM)?</h2>
  <p style="margin-bottom: 16px;">A Finite State Machine (FSM) is a mathematical model of computation used to design sequential logic circuits. Unlike combinational logic where the output depends solely on current inputs, an FSM's output depends on both current inputs and its current internal state (memory). FSMs are the backbone of complex digital systems, from simple traffic light controllers to the complex control units inside modern CPUs.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">How to Use the SQGate FSM Designer</h3>
  <p style="margin-bottom: 16px;">Our visual FSM Designer lets you draw state diagrams right in your browser. Double-click the canvas to create a new state (represented as a circle). You can rename states by clicking on their labels. To create transitions, click and drag from the edge of one state to another. Label your transitions with input conditions (e.g., <code>1</code> or <code>0</code>) and output values. The tool supports both Moore machines (outputs tied to states) and Mealy machines (outputs tied to transitions).</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">Automatic HDL Generation</h3>
  <p style="margin-bottom: 16px;">The true power of this tool lies in its automatic code generation. Once you have drawn your state diagram and defined your reset state, click the "Generate Verilog" button. The engine will parse your graphical model and instantly output clean, synthesizable Verilog HDL code using standard three-process FSM coding styles (state register, next-state combinational logic, and output logic). This is an invaluable tool for VLSI students aiming to bridge the gap between concept and hardware implementation.</p>
</div>
""",
    "puzzle/index.html": """
<!-- UNIQUE TOOL CONTENT -->
<div class="tool-article" style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px; color: rgba(255,255,255,0.8); line-height: 1.7; font-family: var(--font-sans);">
  <h2 style="color: #fff; font-size: 24px; margin-bottom: 16px;">Mastering Digital Logic through Puzzles</h2>
  <p style="margin-bottom: 16px;">Logic Quest is an educational puzzle game designed to test your understanding of Boolean logic and universal gates. When learning digital electronics, simply memorizing truth tables isn't enough; you need to understand how different logic gates interact to synthesize specific behaviors. This gamified sandbox challenges you to recreate complex truth tables using a limited inventory of basic logic gates.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">How to Play Logic Quest</h3>
  <p style="margin-bottom: 16px;">Each level presents you with a target truth table (a set of inputs A, B, C and a desired output Q). Your goal is to wire together logic gates from your available inventory at the bottom of the screen to achieve that exact output. Drag gates onto the canvas, connect their input and output nodes, and watch the live simulation update your current truth table. If your output perfectly matches the target truth table, you beat the level!</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">The Power of Universal Gates</h3>
  <p style="margin-bottom: 16px;">Many of the advanced levels restrict you to using only NAND or NOR gates. This is a practical lesson in functional completeness. Because NAND and NOR are universal gates, any possible digital circuit—no matter how complex—can be built entirely out of them. Solving these levels will train your brain to quickly apply De Morgan's Laws and Boolean algebraic transformations on the fly, a crucial skill for digital design interviews and exams.</p>
</div>
""",
    "circuit-simulator/index.html": """
<!-- UNIQUE TOOL CONTENT -->
<div class="tool-article" style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px; color: rgba(255,255,255,0.8); line-height: 1.7; font-family: var(--font-sans);">
  <h2 style="color: #fff; font-size: 24px; margin-bottom: 16px;">Interactive Digital Logic Simulator</h2>
  <p style="margin-bottom: 16px;">Our browser-based digital circuit simulator provides a full sandbox for prototyping and testing logic designs. Whether you are a computer science student learning about basic AND/OR gates or an electrical engineer sketching out a complex ALU data path, this tool allows you to wire up components and observe signal propagation in real-time without needing to install heavy EDA software like Logisim or Multisim.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">How to Build Your First Circuit</h3>
  <p style="margin-bottom: 16px;">To start building, open the component menu on the left sidebar. Drag basic inputs (like toggle switches or push buttons) and logic gates (AND, OR, XOR, NAND) onto the infinite canvas. To wire components together, click and drag from an output node (usually on the right side of a gate) to an input node. Finally, connect the final gate to an output component like an LED or 7-segment display. Flip the input switches to watch the signal states (0 or 1) propagate through the wires instantly.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">Advanced Features: Clocks & Sequential Logic</h3>
  <p style="margin-bottom: 16px;">Beyond simple combinational logic, our simulator fully supports sequential circuits. You can drop in a Clock Generator and wire it to the clock pins of D Flip-Flops, SR Latches, or JK Flip-Flops to build counters and shift registers. The simulator evaluates states at microsecond intervals, allowing you to debug race conditions, observe state changes on the rising edge, and fully understand synchronous memory elements.</p>
</div>
""",
    "truth-table-generator/index.html": """
<!-- UNIQUE TOOL CONTENT -->
<div class="tool-article" style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px; color: rgba(255,255,255,0.8); line-height: 1.7; font-family: var(--font-sans);">
  <h2 style="color: #fff; font-size: 24px; margin-bottom: 16px;">Boolean Expression to Truth Table Generator</h2>
  <p style="margin-bottom: 16px;">A Truth Table is the most fundamental way to describe the behavior of a digital logic circuit. It explicitly lists every possible combination of input variables and the resulting output. Our automated Truth Table Generator instantly parses any Boolean algebra expression you type and calculates the full truth table, saving you from tedious manual computation and human error during complex logic design.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">How to Use the Generator</h3>
  <p style="margin-bottom: 16px;">Simply type your Boolean expression into the input box. The parser understands standard digital logic notation. Use `*` or `&` for AND, `+` or `|` for OR, `^` for XOR, and `'` or `~` for NOT (negation). For example, to generate a table for a half adder's sum output, you would type <code>A^B</code>. The generator automatically detects the unique variables in your expression, calculates the 2^n input permutations, and generates a cleanly formatted table.</p>
  <h3 style="color: #fff; font-size: 20px; margin-top: 32px; margin-bottom: 16px;">Minterms and Maxterms Analysis</h3>
  <p style="margin-bottom: 16px;">In addition to the raw table output, the generator analyzes the final column to automatically extract the Canonical Sum of Products (SOP) and Canonical Product of Sums (POS). It will list the specific minterms (where the output is 1) and maxterms (where the output is 0). This makes it incredibly easy to take a raw algebraic expression and immediately map it into our Karnaugh Map solver for further minimization.</p>
</div>
"""
}

# Regex to find the generic SEO block
seo_block_regex = r'<div style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px;">.*?<!-- SEO TOOL DESCRIPTIONS FOR ADSENSE CRAWLER.*?</div>\s*</div>\s*</div>'

for rel_path, article in contents.items():
    file_path = os.path.join(base_dir, rel_path)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Try to find and replace the generic SEO block
        if "SEO TOOL DESCRIPTIONS" in content:
            # We can use regex or string parsing. 
            # A simpler way is to just find the start of the generic block and replace everything to the end of it.
            # But the generic block starts at `<div style="max-width: 1200px; margin: 0 auto 64px auto; padding: 0 24px;">`
            # and ends before `<div class="toast" id="toast"></div>` or `<script>` or `</body>`
            # Let's just find the start:
            start_marker = '<!-- SEO TOOL DESCRIPTIONS FOR ADSENSE CRAWLER (BOTTOM) -->'
            if start_marker in content:
                # Replace the entire block
                # The block might be inside a div or just before the footer
                idx = content.find(start_marker)
                # find the end of the block, which is usually the last </div> before <script> or <div class="toast">
                end_idx = content.find('<script>', idx)
                toast_idx = content.find('<div class="toast"', idx)
                
                real_end = end_idx
                if toast_idx != -1 and toast_idx < end_idx:
                    real_end = toast_idx
                
                # Before real_end, there should be a closing </div> for the wrapper. We just replace everything between idx-something to real_end
                # Actually, the start_marker is just a comment. Let's just do a string replace of the known generic block structure.
                # To be safe, we'll just insert our article BEFORE the toast/script, and remove the generic block.
            
            # Since the generic block is exactly 27 lines, let's just use regex to nuke the old one.
            content = re.sub(r'<!-- SEO TOOL DESCRIPTIONS FOR ADSENSE CRAWLER.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
            
        # Now, insert our unique content right before </body>, or before <script>
        if '</body>' in content:
            content = content.replace('</body>', article + '\n</body>')
        else:
            content += article
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected unique content into {rel_path}")
    else:
        print(f"File not found: {file_path}")
