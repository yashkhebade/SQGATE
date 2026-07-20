import re

file_path = r"C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Trim meta keywords
old_keywords = '<meta name="keywords" content="logic gate simulator online, FSM designer, finite state machine Verilog export, Karnaugh map solver, Boolean algebra simplification, digital electronics tools, online circuit simulator, logic puzzle game, digital logic design, EDA tools online, truth table generator, combinational circuit simulator, sequential circuit design, GATE exam preparation tools, engineering student tools, K-map solver 6 variable, logic circuit visualization, flip flop simulator, state machine diagram, Verilog code generator, digital electronics for ECE, BTech digital electronics, online digital logic simulator, free EDA software, gate level simulation, Boolean expression minimizer, logic gate puzzle, HDL learning tool, digital circuit design online, clocked circuit simulator, synchronous circuit design, asynchronous FSM, NAND NOR gate simulator, multiplexer simulator, decoder encoder circuit, half adder full adder, binary logic simulator" />'
new_keywords = '<meta name="keywords" content="logic gate simulator, FSM designer, Karnaugh map solver, digital logic design, truth table generator, Verilog export" />'

content = content.replace(old_keywords, new_keywords)

# 2. Consolidate marketing sections
# Find the start of `<article class="publisher-content"` and the end of `</section>` (line 10440)
start_marker = '<article class="publisher-content" style="padding: 60px 5%; max-width: 900px; margin: 0 auto; color: var(--t2); font-family: var(--fsans); line-height: 1.6;">'
end_marker = '  </section>'

idx_start = content.find(start_marker)
idx_end = content.find(end_marker, idx_start)

if idx_start != -1 and idx_end != -1:
    idx_end += len(end_marker)
    
    consolidated_html = """  <article class="publisher-content" style="padding: 60px 5%; max-width: 900px; margin: 0 auto; color: var(--t2); font-family: var(--fsans); line-height: 1.6;">
    <h2 style="color: #fff; font-size: 28px; margin-bottom: 24px;">Complete Digital Logic Toolkit</h2>
    <p style="margin-bottom: 16px;">SQGate is an educational sandbox designed for engineering students and hobbyists to master digital electronics directly in the browser. Without installing heavy EDA software, you can prototype complex combinational and sequential logic circuits, evaluate real-time signal propagation, and perform rigorous timing analysis using the integrated waveform viewer.</p>
    <h3 style="color: #fff; font-size: 22px; margin-top: 32px; margin-bottom: 16px;">From Schematic to Hardware</h3>
    <p style="margin-bottom: 16px;">Bridge the gap between theoretical Boolean algebra and actual hardware synthesis. SQGate features specialized tools for drawing finite state machines (FSMs), solving Karnaugh maps up to 6 variables, and generating truth tables automatically. Once your circuit or state machine is verified, instantly export it to clean, synthesizable Verilog HDL code, ready to be deployed onto a physical FPGA.</p>
    <div style="margin-top: 40px; padding: 20px; background: rgba(139, 92, 246, 0.1); border-radius: 8px; border: 1px solid rgba(139, 92, 246, 0.2);">
      <h4 style="color: #fff; margin-bottom: 12px;">Engineering Resources</h4>
      <p style="margin-bottom: 0;">Explore our <a href="/blog/" style="color: #a78bfa; text-decoration: underline;">Educational Blog</a> for comprehensive Masterclasses on state machine design, logic minimization, and CPU architecture.</p>
    </div>
  </article>"""
    
    content = content[:idx_start] + consolidated_html + content[idx_end:]
    
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html keywords and marketing copy.")
