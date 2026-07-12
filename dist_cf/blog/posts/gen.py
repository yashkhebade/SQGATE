import re
import datetime
import os

template_path = r'C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\template.html'
output_path = r'C:\Users\Admin\.gemini\antigravity\worktrees\resilient-hertz\apply-code-changes\blog\posts\how-to-solve-karnaugh-maps.html'

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

META_TITLE = 'How to Solve Karnaugh Maps (K-Maps) Step-by-Step | SQGATE'
META_DESCRIPTION = 'A highly technical, comprehensive guide on solving Karnaugh Maps (K-Maps) for Boolean logic simplification. Learn rules, grouping, and advanced variables.'
META_KEYWORDS = 'Karnaugh Map, K-Map, Boolean Algebra, Logic Design, Prime Implicants, Digital Electronics, SQGATE, 4-variable K-Map, Don\'t Care Conditions'
CANONICAL_URL = 'https://sqgate.online/blog/posts/how-to-solve-karnaugh-maps.html'
TITLE = 'How to Solve Karnaugh Maps (K-Maps) Step-by-Step: The Ultimate Engineering Guide'
AUTHOR = 'Hardware Engineering Team'
DATE = 'July 2, 2026'
READ_TIME = '15 min read'

SCHEMA_JSON = '''{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "How to Solve Karnaugh Maps (K-Maps) Step-by-Step: The Ultimate Engineering Guide",
  "author": {
    "@type": "Organization",
    "name": "SQGATE Engineering"
  },
  "datePublished": "2026-07-02",
  "image": [
    "https://sqgate.online/blog/posts/images/karnaugh_map_1782910176565.png"
  ]
}'''

CONTENT = '''
<p>In digital logic design, the simplification of Boolean algebraic expressions is a foundational task. While Boolean algebra provides analytical rules for minimizing logic circuits, Karnaugh Maps (K-Maps) offer a more intuitive, visual method for finding the minimal sum-of-products (SOP) or product-of-sums (POS) expressions. Developed by Maurice Karnaugh in 1953, the K-Map translates truth tables into a two-dimensional grid where adjacent cells represent minterms that differ by exactly one Boolean variable. This property, rooted in Gray code ordering, guarantees that visually adjacent cells can be logically simplified.</p>

<img src="images/karnaugh_map_1782910176565.png" alt="Karnaugh Map Visualization" />

<h2>1. The Theoretical Underpinnings of Karnaugh Maps</h2>
<p>At the core of Karnaugh mapping is the fundamental Boolean theorem of adjacency: <code>A B + A B' = A (B + B') = A</code>. This theorem dictates that if two product terms differ in only one variable, that variable can be eliminated. In an algebraic context, finding all such pairs can be exhaustive and error-prone. The K-Map structurally organizes minterms such that any two adjacent cells (horizontally or vertically) differ by only one variable, making the application of this theorem trivial.</p>

<p>The grid itself is a topological torus; the top and bottom edges are adjacent, as are the left and right edges. This wrapping reflects the cyclic nature of Gray code. For a function of <em>n</em> variables, the K-Map contains 2<sup><em>n</em></sup> cells. Each cell corresponds to a specific combination of inputs. When evaluating a Boolean function, we place a "1" in cells corresponding to the function's minterms (for SOP) and a "0" for maxterms (for POS). The remaining cells are filled accordingly, with "Don't Care" conditions denoted by an "X" or "d".</p>

<p>To truly grasp the power of the K-Map, we must delve deeper into the mathematical structure it represents. The layout of the Karnaugh map is effectively a planar representation of an <em>n</em>-dimensional hypercube, where each vertex represents a unique state of the Boolean variables. When you group adjacent 1s in a K-Map, you are essentially identifying subcubes (edges, faces, or volumes) within this hypercube where the function evaluates to true regardless of the value of the dimension traversed. By finding the largest possible subcubes, we obtain the smallest possible logic gates to implement the function.</p>

<h2>2. Fundamental Rules of Grouping</h2>
<p>The simplification process relies on grouping adjacent 1s (for SOP). The rules for grouping are stringent and dictate the optimality of the final expression:</p>
<ul>
  <li><strong>Group Sizes:</strong> Groups must contain 2<sup><em>k</em></sup> cells, where <em>k</em> is an integer (e.g., 1, 2, 4, 8, 16). A group of 2 eliminates 1 variable, a group of 4 eliminates 2 variables, and so forth.</li>
  <li><strong>Shape of Groups:</strong> Groups must be rectangular or square. Diagonal grouping is strictly forbidden because diagonal cells differ by two or more variables, violating the adjacency theorem.</li>
  <li><strong>Maximal Grouping:</strong> Always form the largest possible group. A sub-optimal smaller group will result in redundant logic gates in the final circuit implementation.</li>
  <li><strong>Overlap:</strong> Groups can and should overlap if it helps in forming larger groups. An overlap simply means a minterm is covered by multiple product terms, which is perfectly valid in Boolean algebra (since A + A = A).</li>
  <li><strong>Wraparound:</strong> As mentioned, the map is a torus. The leftmost column is adjacent to the rightmost column, and the top row is adjacent to the bottom row. Four corners of a 4-variable map form a valid group of 4.</li>
  <li><strong>Cover All 1s:</strong> Every "1" on the map must be included in at least one group.</li>
</ul>

<h2>3. Prime Implicants and Essential Prime Implicants</h2>
<p>To write highly technical documentation on K-Maps, one must distinguish between implicants, prime implicants, and essential prime implicants. An <em>implicant</em> is any product term that implies the function is true. Graphically, it is any valid group of 1s in the K-Map. A <em>prime implicant (PI)</em> is a group of 1s that cannot be combined with any other group to form a larger group. In circuit terms, a PI is a candidate for the final minimal expression.</p>
<p>An <em>essential prime implicant (EPI)</em> is a prime implicant that covers at least one "1" that is not covered by any other prime implicant. The process of extracting the minimal Boolean equation revolves around first identifying all prime implicants, selecting all essential prime implicants (which MUST be in the final equation), and then judiciously choosing from the remaining prime implicants to cover any leftover 1s with the fewest possible terms.</p>

<h2>4. Solving the 2-Variable and 3-Variable K-Map</h2>
<p>The 2-variable K-Map (A, B) consists of 4 cells. It is trivial but foundational. The variables are typically assigned to the rows and columns. A single 1 yields a 2-variable term. A group of two 1s yields a 1-variable term. A group of four 1s yields a logical constant "1".</p>
<p>The 3-variable K-Map (A, B, C) consists of 8 cells, typically arranged as 2 rows and 4 columns. The column headers follow Gray code: 00, 01, 11, 10. The jump from 01 to 11 is critical; if standard binary (00, 01, 10, 11) were used, the middle two columns would differ by two variables (changing from 01 to 10 involves changing both bits), breaking the adjacency required for visual simplification. When solving a 3-variable map, one must be vigilant for wraparounds on the left and right edges.</p>

<p>Consider the Boolean function F(A, B, C) = &Sigma;m(0, 2, 4, 6). Filling the K-Map, we find 1s at binary positions 000, 010, 100, and 110. In a 2x4 grid, these populate the outermost columns (00 and 10). Because the map wraps around, these four cells are contiguous. Grouping them together forms a group of 4. Analyzing the variables, A changes (0 to 1), B changes (0 to 1), but C remains constant at 0. Therefore, the simplified expression is F = C'.</p>

<h2>5. Mastering the 4-Variable K-Map</h2>
<p>The 4-variable K-Map (A, B, C, D) is the workhorse of undergraduate logic design and everyday discrete component engineering. It consists of 16 cells in a 4x4 matrix. The rows are indexed by AB (00, 01, 11, 10) and columns by CD (00, 01, 11, 10). The geometric complexities increase here, as wraparounds can occur horizontally, vertically, and in all four corners simultaneously.</p>
<p>Let's walk through a comprehensive example. Suppose we have the following truth table function: F(A,B,C,D) = &Sigma;m(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14).
1. Setup the 4x4 map.
2. Place 1s in cells: 0(0000), 1(0001), 2(0010), 4(0100), 5(0101), 6(0110), 8(1000), 9(1001), 12(1100), 13(1101), 14(1110).
3. Identify Essential Prime Implicants. The group covering the left half of the map (cells 0, 1, 4, 5, 8, 9, 12, 13) forms an massive 2x4 rectangle. This is a group of 8. The variables C and D span all four Gray code combinations, so they drop out. The variable B spans 0 and 1, so it drops out. Only A's value... wait, looking closely at cells 0,4,8,12 (column 00) and 1,5,9,13 (column 01), they cover C=0. So C=0 is constant. Thus, this group of 8 simplifies to C'.
4. Next, we have remaining 1s at 2, 6, 14. We can group (2, 6, 14, 10)? Wait, 10 is not a minterm. We can group (2, 6) with (0, 4) - wraparound! That's a group of 4: A'D'. We can also group (6, 14) with (4, 12) - a group of 4: BD'.
5. By ensuring all 1s are covered by the largest groups, the final minimal SOP expression becomes F = C' + A'D' + BD'.</p>

<h2>6. Don't Care Conditions: The Engineer's Best Friend</h2>
<p>In real-world digital systems, certain input combinations may never occur. For instance, in a BCD (Binary-Coded Decimal) circuit, the input states 1010 through 1111 (decimal 10 to 15) are invalid. The outputs for these states are entirely irrelevant to the system's operation. These are termed "Don't Care" conditions, represented by an 'X' in the truth table and K-Map.</p>
<p>Don't Cares provide incredible leverage for optimization. When formulating prime implicants, an engineer can selectively treat an 'X' as a '1' if it enables the formation of a larger group, or treat it as a '0' if it doesn't help. The rule of thumb is: never circle an 'X' unless it expands an existing group of 1s to the next power of two. Grouping 'X's purely by themselves serves no purpose other than adding unnecessary logic gates.</p>

<h2>7. Beyond 4 Variables: 5 and 6 Variable Maps</h2>
<p>While K-Maps are highly effective up to 4 variables, scaling them up requires three-dimensional visualization. A 5-variable K-Map (A, B, C, D, E) contains 32 cells and is typically drawn as two 4-variable maps side-by-side. One map represents A=0 and the other represents A=1. The standard adjacency rules apply within each map, but there is an additional adjacency: corresponding cells between the two maps are adjacent. You must mentally overlay the two planes to identify 3D groupings.</p>
<p>A 6-variable K-Map (A, B, C, D, E, F) comprises 64 cells, organized as a 2x2 matrix of 4-variable maps. Groupings can occur within maps, between adjacent maps horizontally or vertically, but NOT diagonally. Beyond 6 variables, visual methods completely break down. The human brain struggles to process higher-dimensional adjacency. At this threshold, algorithmic approaches like the Quine-McCluskey method or heuristic logic minimizers (like Espresso) become strictly necessary.</p>

<h2>8. Integrating with SQGATE</h2>
<p>After minimizing your Boolean expression, the next step is circuit implementation. Our SQGATE simulator allows you to rapidly transition from theoretical equations to functional digital circuits. Here is a JSON snippet representing a simplified circuit exported directly into SQGATE format.</p>

<pre><code>{
  "version": "1.1",
  "project": "K-Map Minimal Circuit",
  "components": [
    {"id": "inA", "type": "INPUT", "x": 50, "y": 100},
    {"id": "inB", "type": "INPUT", "x": 50, "y": 200},
    {"id": "inC", "type": "INPUT", "x": 50, "y": 300},
    {"id": "notC", "type": "NOT", "x": 150, "y": 300},
    {"id": "and1", "type": "AND", "x": 300, "y": 150},
    {"id": "or1", "type": "OR", "x": 450, "y": 200},
    {"id": "outF", "type": "OUTPUT", "x": 600, "y": 200}
  ],
  "wires": [
    {"from": "inC", "to": "notC"},
    {"from": "inA", "to": "and1"},
    {"from": "inB", "to": "and1"},
    {"from": "and1", "to": "or1"},
    {"from": "notC", "to": "or1"},
    {"from": "or1", "to": "outF"}
  ]
}</code></pre>

<h2>9. Sum of Products vs Product of Sums</h2>
<p>Most engineers default to Sum of Products (SOP) by circling the 1s in the K-map. This leads to a two-level AND-OR implementation. However, finding the Product of Sums (POS) is equally viable and sometimes yields a more economical circuit. To solve for POS, you circle the 0s instead of the 1s. This gives you the minimized SOP expression for the complement of the function (F'). By applying De Morgan's Laws to F', you invert the expression to arrive at the minimal POS form, which manifests as an OR-AND circuit topology. Depending on the density of 1s versus 0s, POS might require significantly fewer logic gates.</p>

<h2>10. Common Pitfalls and Troubleshooting in K-Map Minimization</h2>
<p>Despite its graphical simplicity, students and engineers alike often stumble when applying K-Maps. Here are the most prevalent errors:</p>
<ol>
  <li><strong>Sub-optimal Grouping:</strong> Failing to notice edge wraparounds (especially corners) leads to groups of 2 instead of 4, or groups of 4 instead of 8. This directly translates to extraneous gates and inputs.</li>
  <li><strong>Redundant Groups:</strong> Including a prime implicant that is not essential, and whose 1s are already entirely covered by other essential prime implicants. This creates duplicate logic paths that serve no logical purpose.</li>
  <li><strong>Incorrect Transcription:</strong> Misplacing minterms when transferring data from a truth table to the K-Map. Because K-Map columns (and rows) are ordered in Gray code (00, 01, 11, 10), it is remarkably easy to accidentally place the minterm for '10' into the '11' column. Always double-check coordinate mapping.</li>
  <li><strong>Misinterpreting Don't Cares:</strong> Forcing a group to include all 'X's. Remember, 'X's are wildcards designed to help you, not burdens you are obligated to cover.</li>
  <li><strong>Variable Inversion Errors:</strong> When extracting the algebraic term from a group, failing to correctly invert variables that are 0 for that group. If a group resides exclusively in row A=0, the corresponding term MUST include A', not A.</li>
</ol>

<h2>11. Hardware Engineering Implications: Static Hazards</h2>
<p>In high-speed digital circuit design, physical delays in logic gates become critical. While a K-Map minimizes logic, a fully minimized SOP circuit can suffer from static hazards. A static-1 hazard occurs when an output is supposed to remain at logic '1' during a single-variable input transition, but momentarily dips to '0' due to unequal propagation delays through different paths of the combinational circuit. </p>
<p>Interestingly, K-Maps are the perfect tool for identifying and resolving static hazards. A static hazard exists if there are adjacent 1s in the K-Map that are not covered by the same prime implicant group. As the input transitions between these two adjacent states, the circuit physically switches between two different product terms. If the new product term is slightly slower to evaluate to '1' than the old product term evaluates to '0', the output glitches. To fix this, a hardware engineer will intentionally add a redundant prime implicant (a consensus term) to the Boolean expression, specifically grouping those adjacent cells to bridge the gap. This violates the goal of absolute minimization, but it is a necessary trade-off to ensure signal integrity and glitch-free operation in asynchronous logic design.</p>

<h2>12. Conclusion</h2>
<p>The Karnaugh Map remains an indispensable technique in the hardware engineer's toolkit. It bridges the gap between abstract Boolean algebra and tangible circuit synthesis, providing a visually intuitive method for achieving optimal logic minimization. While algorithmic minimization software has taken over for massively complex, high-variable designs, the fundamental understanding of logic adjacency, prime implicants, and boolean simplification imparted by mastering K-Maps is irreplaceable. By internalizing these graphical rules, engineers can instinctively optimize smaller control circuits, debug state machines, and preemptively resolve hardware glitches with unparalleled efficiency.</p>
<p>We encourage you to practice these concepts using our interactive tools. The transition from theoretical simplification to functional simulation is the cornerstone of robust digital design.</p>
'''

final_html = template.replace('{{META_TITLE}}', META_TITLE)
final_html = final_html.replace('{{META_DESCRIPTION}}', META_DESCRIPTION)
final_html = final_html.replace('{{META_KEYWORDS}}', META_KEYWORDS)
final_html = final_html.replace('{{CANONICAL_URL}}', CANONICAL_URL)
final_html = final_html.replace('{{TITLE}}', TITLE)
final_html = final_html.replace('{{AUTHOR}}', AUTHOR)
final_html = final_html.replace('{{DATE}}', DATE)
final_html = final_html.replace('{{READ_TIME}}', READ_TIME)
final_html = final_html.replace('{{SCHEMA_JSON}}', SCHEMA_JSON)
final_html = final_html.replace('{{CONTENT}}', CONTENT)
final_html = final_html.replace('https://sqgate.online/og-image.png', 'https://sqgate.online/blog/posts/images/karnaugh_map_1782910176565.png')

GA_SCRIPT = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
</script>
'''

if GA_SCRIPT not in final_html:
    final_html = final_html.replace('</head>', GA_SCRIPT + '</head>')

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Successfully generated HTML.')
