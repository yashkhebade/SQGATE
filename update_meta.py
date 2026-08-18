import re
import os

pages = {
    'k-map/index.html': {
        'title': 'Karnaugh Map Solver (up to 6 variables) | SQGATE',
        'desc': 'Interactive online K-Map solver. Simplify Boolean algebra expressions visually with support for up to 6 variables. Find prime implicants and SOP instantly.'
    },
    'fsm/index.html': {
        'title': 'Finite State Machine (FSM) Designer | SQGATE',
        'desc': 'Draw Moore and Mealy state diagrams and automatically generate synthesizable Verilog HDL code. Free online FSM designer and simulator.'
    },
    'puzzle/index.html': {
        'title': 'Logic Quest - Educational Puzzle Game | SQGATE',
        'desc': 'Master digital logic through gamification. Solve logic gate puzzles using restricted components to build specific truth tables and minimize expressions.'
    },
    'circuit-simulator/index.html': {
        'title': 'Visual Logic Gate Circuit Simulator | SQGATE',
        'desc': 'Free online digital electronics simulator. Build combinational and sequential logic circuits with an intuitive drag-and-drop interface. No install required.'
    },
    'truth-table-generator/index.html': {
        'title': 'Truth Table Generator & Evaluator | SQGATE',
        'desc': 'Instantly generate truth tables for complex Boolean logic expressions. Evaluate and analyze combinational logic networks online for free.'
    }
}

for filepath, meta in pages.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace or add title
    if '<title>' in content:
        content = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', content, flags=re.DOTALL|re.IGNORECASE)
    else:
        content = content.replace('</head>', f'  <title>{meta["title"]}</title>\n</head>')
        
    # Replace or add meta description
    if 'name="description"' in content:
        content = re.sub(r'<meta[^>]+name="description"[^>]*>', f'<meta name="description" content="{meta["desc"]}">', content, flags=re.IGNORECASE)
    else:
        content = content.replace('</head>', f'  <meta name="description" content="{meta["desc"]}">\n</head>')
        
    # Replace or add canonical
    canonical_url = f'https://sqgate.online/{filepath.replace("/index.html", "")}'
    if 'rel="canonical"' in content:
        content = re.sub(r'<link[^>]+rel="canonical"[^>]*>', f'<link rel="canonical" href="{canonical_url}">', content, flags=re.IGNORECASE)
    else:
        content = content.replace('</head>', f'  <link rel="canonical" href="{canonical_url}">\n</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Meta tags updated successfully.")
