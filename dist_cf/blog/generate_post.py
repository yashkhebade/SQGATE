import os

template_path = r'C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\template.html'
out_path = r'C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\posts\adv-part2-multipliers.html'

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements
html = html.replace('{{TITLE}}', 'Part 2: Hardware Multipliers & Dividers')
html = html.replace('{{META_TITLE}}', 'Designing Hardware Multipliers')
html = html.replace('{{META_DESCRIPTION}}', 'How ALUs perform fast multiplication using array multipliers, Wallace trees, and shift-and-add algorithms.')
html = html.replace('{{META_KEYWORDS}}', 'hardware multiplier, array multiplier, Wallace tree, ALU design')
html = html.replace('{{CANONICAL_URL}}', 'https://sqgate.online/blog/posts/adv-part2-multipliers.html')
html = html.replace('{{AUTHOR}}', 'SQGATE Engineering')
html = html.replace('{{DATE}}', 'July 2, 2026')
html = html.replace('{{READ_TIME}}', '13 min read')
html = html.replace('https://sqgate.online/og-image.png', 'https://sqgate.online/blog/posts/images/module4_alu_render_1782750594712.png')
html = html.replace('{{SCHEMA_JSON}}', '{}')

# Add Google Analytics to head
ga_code = '''
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-SQGATE1234"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-SQGATE1234');
  </script>
</head>'''
html = html.replace('</head>', ga_code)

content = '''
<h2>Introduction to Hardware Arithmetic</h2>
<p>In our previous exploration of advanced hardware architectures, we delved into instruction pipelining and how it maximizes CPU throughput by overlapping instruction execution. Today, in Part 2 of our series, we focus on the intricate and fundamental operations of Arithmetic Logic Units (ALUs): hardware multiplication and division.</p>
<p>While addition and subtraction form the backbone of binary arithmetic, multiplication and division represent a significant leap in complexity. In software, these operations are abstracted away by simple operators like <code>*</code> and <code>/</code>. However, at the hardware level, multiplying two 32-bit or 64-bit integers requires a staggering number of parallel operations to complete within a single clock cycle, or necessitates complex iterative state machines. Designing an efficient hardware multiplier or divider is a masterclass in balancing area (transistor count), power consumption, and propagation delay.</p>

<img src="images/module4_alu_render_1782750594712.png" alt="Hardware Multiplier">

<h2>The Anatomy of Binary Multiplication</h2>
<p>At its core, binary multiplication is functionally identical to the long multiplication you learned in grade school, albeit restricted to base-2 digits (0 and 1). When you multiply an N-bit multiplicand by an M-bit multiplier, the result requires N+M bits to prevent overflow. The process involves two primary steps:</p>
<ol>
  <li><strong>Partial Product Generation:</strong> Each bit of the multiplier is multiplied by the entire multiplicand. Since binary digits are only 0 or 1, a partial product is either a copy of the multiplicand (shifted to the correct weight) or all zeros. In hardware, this is beautifully simple: it's just a massive array of parallel AND gates.</li>
  <li><strong>Partial Product Accumulation (Reduction):</strong> The generated partial products must be summed together. This is where the true complexity lies. Summing multiple rows of binary numbers requires a sophisticated network of adders.</li>
</ol>

<h3>The Shift-and-Add Multiplier (Iterative Approach)</h3>
<p>The most straightforward hardware implementation is the shift-and-add multiplier. This iterative architecture uses a single adder, a shift register for the multiplicand, a shift register for the multiplier, and an accumulator for the product.</p>
<p>In each clock cycle, the system checks the least significant bit (LSB) of the multiplier. If it's 1, the multiplicand is added to the accumulator. Regardless of the bit's value, the multiplicand is shifted left (multiplied by 2), and the multiplier is shifted right (divided by 2). This process repeats for N cycles.</p>
<p><strong>Pros:</strong> Extremely low area overhead. It uses a single N-bit adder and some registers.</p>
<p><strong>Cons:</strong> Extremely slow. An N-bit multiplication requires N clock cycles, making it unsuitable for modern high-performance ALUs.</p>

<h3>Array Multipliers (Combinational Approach)</h3>
<p>To eliminate the latency of iterative multipliers, designers turn to combinational Array Multipliers. An array multiplier spatially unrolls the shift-and-add process into a massive 2D grid of full adders and half adders.</p>
<p>In an NxN array multiplier, N partial products are generated simultaneously using N² AND gates. These partial products are then fed into an array of N-1 rows of adders. The carry bits propagate horizontally to the left, while the sum bits propagate diagonally downwards.</p>
<p>While an array multiplier calculates the product in a single clock cycle, it suffers from a significant critical path. The worst-case delay propagates from the top-right corner to the bottom-left corner of the array, passing through O(N) adder stages. For a 32x32 multiplier, this delay becomes the bottleneck for the entire CPU clock frequency.</p>

<h3>Wallace Tree Multipliers (Tree Reduction)</h3>
<p>The Wallace Tree (and its cousin, the Dadda Tree) revolutionizes partial product reduction by shifting from a linear O(N) delay to a logarithmic O(log N) delay. Instead of summing rows sequentially, a Wallace tree sums columns in parallel.</p>
<p>The core building block of a Wallace tree is the Full Adder (FA), which takes three input bits of the same weight and produces a sum bit (same weight) and a carry bit (weight + 1). This is known as a 3:2 compressor.</p>
<p>The Wallace tree algorithm proceeds in stages:</p>
<ol>
  <li>Group the bits in each column into sets of three.</li>
  <li>Feed each group of three into a Full Adder, producing a sum and a carry for the next column.</li>
  <li>Any remaining sets of two bits are fed into a Half Adder (2:2 compressor).</li>
  <li>Single bits are passed unchanged to the next stage.</li>
  <li>Repeat this process until only two rows of partial products remain.</li>
</ol>
<p>Once the tree reduces the matrix to just two rows, a fast Carry-Lookahead Adder (CLA) or Prefix Adder is used to compute the final sum. The Wallace tree minimizes the critical path, enabling the blisteringly fast single-cycle multipliers found in modern architectures.</p>

<h3>Booth's Multiplication Algorithm (Radix-4)</h3>
<p>Even with Wallace trees, an NxN multiplier requires generating N partial products. For a 64-bit multiplier, summing 64 rows is still a massive undertaking. Radix-4 Booth Encoding halves the number of partial products before the reduction tree even begins.</p>
<p>Booth's algorithm works by examining the multiplier bits in overlapping groups of three. By doing so, it effectively multiplies by digits in the set {-2, -1, 0, 1, 2}. Because -2x is just a left shift and an inversion, and +2x is a left shift, these operations are trivial in hardware.</p>
<p>By encoding the multiplier in Radix-4, a 64-bit multiplication generates only 32 partial products. This drastically reduces the size, power, and delay of the subsequent Wallace tree, making Booth Encoding a standard feature in high-performance ALUs.</p>

<h2>Designing Hardware Dividers</h2>
<p>Division is notoriously the most difficult and power-hungry fundamental arithmetic operation. Unlike multiplication, which can be easily parallelized, division is inherently sequential. You cannot compute the next quotient bit without knowing the result of the previous subtraction.</p>

<h3>Restoring vs. Non-Restoring Division</h3>
<p>The digital equivalent of long division is Restoring Division. In each step, the divisor is shifted and subtracted from the partial remainder. If the result is negative (indicating the divisor was larger), the original remainder must be restored (hence the name), and a 0 is placed in the quotient. If the result is positive, a 1 is placed in the quotient, and the new remainder is kept.</p>
<p>Non-Restoring Division improves upon this by eliminating the costly restoration step. Instead of restoring upon a negative result, the algorithm simply records a negative quotient bit (using signed-digit representation) and in the next step, it adds the divisor instead of subtracting it. This streamlines the control logic and slightly improves performance.</p>

<h3>SRT Division</h3>
<p>Named after Sweeney, Robertson, and Tocher, SRT division is the standard algorithm used in modern floating-point units. It is a Radix-4 (or higher) non-restoring algorithm that computes multiple quotient bits per cycle. It achieves this by using a lookup table to guess the next quotient digits based on the most significant bits of the remainder and divisor. The infamous Pentium FDIV bug in 1994 was caused by five missing entries in the SRT division lookup table.</p>

<h3>Newton-Raphson and Goldschmidt Division</h3>
<p>For high-performance floating-point division, some architectures abandon iterative subtraction entirely. Instead, they frame division as multiplication by a reciprocal: A / B = A * (1 / B).</p>
<p>Algorithms like Newton-Raphson and Goldschmidt use an initial lookup table to guess the reciprocal 1/B. They then use the hardware multiplier to iteratively refine this guess. Because hardware multipliers are so fast, these algorithms converge to full 64-bit precision in just a few cycles, leveraging existing execution units rather than building dedicated division hardware.</p>

<h2>Simulating a 2-bit x 2-bit Multiplier in SQGATE</h2>
<p>To truly understand how partial product generation and accumulation work in practice, let's look at a concrete example. Below is a SQGATE JSON snippet representing a fully combinational 2-bit by 2-bit array multiplier. This design uses 4 AND gates to generate the partial products (A0*B0, A1*B0, A0*B1, A1*B1) and two Half Adders to sum them into a 4-bit product (P3 P2 P1 P0).</p>

<pre><code class="language-json">
{
  "project": "2x2 Combinational Multiplier",
  "version": "1.0",
  "components": [
    { "type": "input", "id": "A0", "x": 100, "y": 100, "label": "A0" },
    { "type": "input", "id": "A1", "x": 100, "y": 150, "label": "A1" },
    { "type": "input", "id": "B0", "x": 100, "y": 250, "label": "B0" },
    { "type": "input", "id": "B1", "x": 100, "y": 300, "label": "B1" },
    { "type": "and", "id": "AND00", "x": 300, "y": 125, "label": "A0*B0" },
    { "type": "and", "id": "AND10", "x": 300, "y": 175, "label": "A1*B0" },
    { "type": "and", "id": "AND01", "x": 300, "y": 275, "label": "A0*B1" },
    { "type": "and", "id": "AND11", "x": 300, "y": 325, "label": "A1*B1" },
    { "type": "half_adder", "id": "HA1", "x": 500, "y": 200, "label": "HA1" },
    { "type": "half_adder", "id": "HA2", "x": 500, "y": 300, "label": "HA2" },
    { "type": "output", "id": "P0", "x": 700, "y": 125, "label": "P0 (LSB)" },
    { "type": "output", "id": "P1", "x": 700, "y": 200, "label": "P1" },
    { "type": "output", "id": "P2", "x": 700, "y": 300, "label": "P2" },
    { "type": "output", "id": "P3", "x": 700, "y": 400, "label": "P3 (MSB)" }
  ],
  "wires": [
    { "from": "A0", "to": "AND00", "toPort": "in1" },
    { "from": "B0", "to": "AND00", "toPort": "in2" },
    { "from": "A1", "to": "AND10", "toPort": "in1" },
    { "from": "B0", "to": "AND10", "toPort": "in2" },
    { "from": "A0", "to": "AND01", "toPort": "in1" },
    { "from": "B1", "to": "AND01", "toPort": "in2" },
    { "from": "A1", "to": "AND11", "toPort": "in1" },
    { "from": "B1", "to": "AND11", "toPort": "in2" },
    { "from": "AND00", "to": "P0" },
    { "from": "AND10", "to": "HA1", "toPort": "A" },
    { "from": "AND01", "to": "HA1", "toPort": "B" },
    { "from": "HA1.S", "to": "P1" },
    { "from": "AND11", "to": "HA2", "toPort": "A" },
    { "from": "HA1.C", "to": "HA2", "toPort": "B" },
    { "from": "HA2.S", "to": "P2" },
    { "from": "HA2.C", "to": "P3" }
  ]
}
</code></pre>
<p>By loading this JSON into the SQGATE simulator, you can toggle the input bits and instantly see the partial products propagate through the AND gates and accumulate in the Half Adders to form the final product.</p>

<div style="margin-top: 40px; display: flex; justify-content: space-between; font-weight: bold;">
  <a href="adv-part1-pipelining.html">⬅ Previous</a> 
  <a href="adv-part3-cache.html">Next ➔</a>
</div>
'''

html = html.replace('{{CONTENT}}', content)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('File written to:', out_path)
