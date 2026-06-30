import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

competitors = [
    {"slug": "circuitverse", "name": "CircuitVerse", "keywords": "circuitverse alternative, free logic simulator, browser-based circuitverse, online logic gates"},
    {"slug": "logisim", "name": "Logisim", "keywords": "logisim alternative online, logisim evolution web, free logisim download alternative, logic gate simulator"},
    {"slug": "falstad", "name": "Falstad Circuit Simulator", "keywords": "falstad alternative, falstad circuit simulator alternative, modern falstad alternative, touch-friendly logic simulator"},
    {"slug": "simulator-io", "name": "simulator.io", "keywords": "simulator.io alternative, logic circuit simulator without login, free simulator.io"},
    {"slug": "logigator", "name": "Logigator", "keywords": "logigator alternative, online logic circuit simulator, webgl logic gates"},
    {"slug": "academo", "name": "Academo Logic Gate Simulator", "keywords": "academo alternative, simple logic gate simulator, beginner logic gate tool"},
    {"slug": "tinkercad", "name": "Tinkercad Circuits", "keywords": "tinkercad logic gates alternative, tinkercad digital electronics alternative, online logic gate tool"},
    {"slug": "truth-table-tools", "name": "Truth Table Tools", "keywords": "truth table tools alternative, truth table generator, digital logic solver"},
    {"slug": "logic-gate-online", "name": "Logic Gate Online", "keywords": "logic gate online alternative, free logic simulator web"},
    {"slug": "cedar-ls", "name": "CEDAR LS", "keywords": "cedar ls alternative, academic logic simulator, university logic gate tool"}
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Mandatory SEO Tags -->
  <title>{name} Alternative - Free Online Logic Gate Simulator | SQGATE</title>
  <meta name="description" content="Looking for a free alternative to {name}? SQGATE is a powerful, modern web-based digital logic circuit simulator. No installation required.">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="https://sqgate.online/{slug}">
  
  <!-- OG Tags -->
  <meta property="og:title" content="{name} Alternative - Free Online Logic Gate Simulator | SQGATE">
  <meta property="og:description" content="Looking for a free alternative to {name}? Try SQGATE - a powerful web-based digital logic circuit simulator.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sqgate.online/{slug}">
  <meta property="og:image" content="https://sqgate.online/og-image.png">

  <!-- Google Analytics Tracking Code (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>

  <!-- Google AdSense Tag -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456" crossorigin="anonymous"></script>

  <!-- Redirect to Homepage after 3 seconds -->
  <meta http-equiv="refresh" content="3; url=/home/">
  
  <style>
    body {{
      background-color: #060813;
      color: #cbd5e1;
      font-family: 'Outfit', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
      text-align: center;
      padding: 20px;
    }}
    h1 {{
      color: #fff;
      font-size: 32px;
      margin-bottom: 15px;
    }}
    p {{
      font-size: 18px;
      color: #94a3b8;
    }}
    .spinner {{
      margin-top: 30px;
      width: 40px;
      height: 40px;
      border: 4px solid rgba(255, 255, 255, 0.1);
      border-left-color: #3b82f6;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}
    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}
  </style>
</head>
<body>
  <h1>Looking for {name}?</h1>
  <p>You are being redirected to SQGATE, the ultimate free web-based alternative for digital logic simulation...</p>
  <div class="spinner"></div>
  
  <script>
    setTimeout(function() {{
      window.location.href = "/home/";
    }}, 3000);
  </script>
</body>
</html>
"""

for comp in competitors:
    folder = os.path.join(ROOT_DIR, comp['slug'])
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    html = template.format(
        name=comp['name'],
        slug=comp['slug'],
        keywords=comp['keywords']
    )
    
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {comp['slug']}/index.html")
