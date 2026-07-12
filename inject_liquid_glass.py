import os
import re

SVG_FILTER = """
<!-- LIQUID GLASS SVGS -->
<svg class="liquid-glass-svg-filter" style="position: absolute; width: 0; height: 0; pointer-events: none;">
  <defs>
    <filter id="liquid-glass-filter" x="0%" y="0%" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.05 0.05" numOctaves="3" result="noise" />
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.15 0" in="noise" result="coloredNoise" />
      <feBlend in="SourceGraphic" in2="coloredNoise" mode="screen" />
    </filter>
  </defs>
</svg>
"""

def inject():
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.html'):
                filepath = os.path.join(root, name)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check if already injected
                if 'liquid-glass.css' in content:
                    continue

                # 1. Inject link before </head>
                link_tag = '  <link rel="stylesheet" href="/css/liquid-glass.css">\n</head>'
                content = content.replace('</head>', link_tag)
                
                # 2. Inject SVG filter after <body>
                if '<body>' in content:
                    content = content.replace('<body>', '<body>\n' + SVG_FILTER)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
if __name__ == '__main__':
    inject()
