import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

competitors = [
    {"slug": "logicly", "name": "Logicly", "keywords": "logicly alternative, free logic simulator, logic gate simulator online, digital electronics simulator"},
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
  
  <title>{name} Alternative - Free Online Logic Gate Simulator | SQGATE</title>
  <meta name="description" content="Looking for a free alternative to {name}? SQGATE is a powerful, modern web-based digital logic circuit simulator. No installation required.">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="https://sqgate.online/{slug}">
  
  <meta property="og:title" content="{name} Alternative - Free Online Logic Gate Simulator | SQGATE">
  <meta property="og:description" content="Looking for a free alternative to {name}? Try SQGATE - a powerful web-based digital logic circuit simulator.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sqgate.online/{slug}">
  <meta property="og:image" content="https://sqgate.online/og-image.png">

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>

  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456" crossorigin="anonymous"></script>

  <meta http-equiv="refresh" content="2; url=/home/">
  
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: #060813;
      color: #cbd5e1;
      font-family: 'Outfit', sans-serif;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    /* Skeleton App Layout */
    .skel-topbar {{
      height: 54px;
      background: rgba(12, 15, 28, 0.8);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      padding: 0 20px;
      gap: 15px;
    }}
    .skel-logo {{
      width: 100px;
      height: 24px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      animation: pulse 1.5s infinite;
    }}
    .skel-tools {{
      margin-left: auto;
      display: flex;
      gap: 10px;
    }}
    .skel-tool {{
      width: 32px;
      height: 32px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 6px;
      animation: pulse 1.5s infinite;
    }}
    
    .skel-main {{
      flex: 1;
      display: flex;
    }}
    .skel-sidebar {{
      width: 260px;
      background: rgba(12, 15, 28, 0.5);
      border-right: 1px solid rgba(255, 255, 255, 0.05);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 15px;
    }}
    .skel-gate {{
      width: 100%;
      height: 40px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      animation: pulse 1.5s infinite;
    }}
    .skel-canvas {{
      flex: 1;
      background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
      background-size: 20px 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}
    .skel-msg {{
      background: rgba(12, 15, 28, 0.9);
      border: 1px solid rgba(139, 92, 246, 0.3);
      padding: 30px 40px;
      border-radius: 12px;
      text-align: center;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
      backdrop-filter: blur(10px);
      z-index: 10;
    }}
    .skel-msg h1 {{
      font-size: 24px;
      color: #fff;
      margin-bottom: 10px;
    }}
    .skel-msg p {{
      color: #94a3b8;
      font-size: 15px;
    }}
    .spinner {{
      margin: 20px auto 0;
      width: 30px;
      height: 30px;
      border: 3px solid rgba(255, 255, 255, 0.1);
      border-left-color: #8b5cf6;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }}
    @keyframes pulse {{
      0% {{ opacity: 0.5; }}
      50% {{ opacity: 0.8; }}
      100% {{ opacity: 0.5; }}
    }}
    @keyframes spin {{
      to {{ transform: rotate(360deg); }}
    }}
  </style>
</head>
<body>
  
  <div class="skel-topbar">
    <div class="skel-logo"></div>
    <div class="skel-tools">
      <div class="skel-tool"></div>
      <div class="skel-tool"></div>
      <div class="skel-tool"></div>
      <div class="skel-tool" style="width: 80px;"></div>
    </div>
  </div>
  
  <div class="skel-main">
    <div class="skel-sidebar">
      <div class="skel-gate"></div>
      <div class="skel-gate"></div>
      <div class="skel-gate"></div>
      <div class="skel-gate" style="margin-top: 20px;"></div>
      <div class="skel-gate"></div>
      <div class="skel-gate"></div>
    </div>
    
    <div class="skel-canvas">
      <div class="skel-msg">
        <h1>Loading Simulator...</h1>
        <p>Redirecting you to SQGATE (Alternative to {name})</p>
        <div class="spinner"></div>
      </div>
    </div>
  </div>

  <script>
    setTimeout(function() {{
      window.location.href = "/home/";
    }}, 2000);
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
