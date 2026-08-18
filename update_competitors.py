# -*- coding: utf-8 -*-
import os

competitors = {
    'logisim': {
        'name': 'Logisim',
        'title': 'Logisim Alternative - Free Online Logic Gate Simulator | SQGATE',
        'content': '''<div style="background: rgba(12, 15, 28, 0.9); padding: 40px; border-radius: 12px; color: #cbd5e1; max-width: 900px; margin: 40px auto; overflow-y: auto; max-height: 80vh;">
            <h1 style="color: #fff; margin-bottom: 20px;">Why SQGATE is the Best Modern Alternative to Logisim</h1>
            <p style="margin-bottom: 15px;">For years, <strong>Logisim</strong> has been the standard educational tool for designing and simulating digital logic circuits. However, Logisim development was officially suspended in 2014. While forks like Logisim-Evolution exist, they still rely on legacy Java environments, require local installation, and often present compatibility issues on modern operating systems like macOS and Windows 11.</p>
            <p style="margin-bottom: 15px;">SQGATE is a modern, 100% web-based alternative to Logisim. Built entirely in HTML5 Canvas and JavaScript, SQGATE requires zero installation. You can launch it directly in your browser, whether you're on a Chromebook, a MacBook, or a Windows PC. It offers the same fundamental educational value—drag-and-drop gates, wiring, and real-time simulation—but with a sleek, hardware-accelerated user interface.</p>
            <p style="margin-bottom: 15px;">One of the biggest advantages of SQGATE over Logisim is its seamless integration of advanced tools. Not only can you build combinational and sequential circuits, but you can also use our built-in Finite State Machine (FSM) designer to graphically map out Moore and Mealy machines. Furthermore, SQGATE features an interactive Karnaugh Map (K-Map) solver that supports up to 6 variables, a feature absent in the original Logisim.</p>
            <p style="margin-bottom: 15px;">When it comes to exporting, SQGATE excels. While Logisim uses its own proprietary XML format (.circ), SQGATE allows you to export your visual circuits directly to structural Verilog HDL. This means the designs you build in SQGATE can be synthesized and deployed to actual FPGAs using industry-standard tools like Xilinx Vivado or Intel Quartus.</p>
            <p style="margin-bottom: 30px;">Make the switch today. Enjoy cloud-like portability (with local offline saving via PWA), a modern dark-mode aesthetic, and powerful HDL generation without ever downloading a .jar file again.</p>
            <a href="/home/" style="display: inline-block; background: #8b5cf6; color: #fff; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold;">Launch SQGATE Simulator Now</a>
        </div>'''
    },
    'tinkercad': {
        'name': 'Tinkercad',
        'title': 'Tinkercad Circuits Alternative for Digital Logic | SQGATE',
        'content': '''<div style="background: rgba(12, 15, 28, 0.9); padding: 40px; border-radius: 12px; color: #cbd5e1; max-width: 900px; margin: 40px auto; overflow-y: auto; max-height: 80vh;">
            <h1 style="color: #fff; margin-bottom: 20px;">SQGATE vs Tinkercad Circuits: Which is Better for Digital Logic?</h1>
            <p style="margin-bottom: 15px;"><strong>Tinkercad Circuits</strong> is a fantastic tool for learning basic electronics, Arduino programming, and breadboarding. It provides a visual, real-world representation of components like resistors, LEDs, and 7400-series IC chips. However, when it comes to purely learning digital logic and boolean algebra, wiring up virtual breadboards in Tinkercad can quickly become a tedious and cluttered mess.</p>
            <p style="margin-bottom: 15px;">SQGATE offers a schematic-based alternative to Tinkercad's physical breadboard layout. Instead of struggling to route dozens of wires to specific pins on a generic IC graphic, SQGATE lets you use standardized IEEE logic gate symbols (AND, OR, NOT, XOR). This abstract schematic capture is exactly how professional VLSI engineers design digital systems.</p>
            <p style="margin-bottom: 15px;">By stripping away the physical analog aspects (like calculating resistor values for LEDs), SQGATE allows students to focus 100% on the boolean logic. You can instantly see the state of every wire (High/Low) without needing to attach virtual multimeters. Our simulation engine evaluates states instantly, making it much faster to debug complex sequential circuits like 8-bit counters or memory arrays.</p>
            <p style="margin-bottom: 15px;">Furthermore, SQGATE provides educational tools that Tinkercad lacks, such as a 6-variable Karnaugh Map solver, an automated Truth Table generator, and a visual Finite State Machine (FSM) designer. If you are a computer science or electrical engineering student moving beyond basic Arduino projects into dedicated digital logic design, SQGATE is the specialized tool you need.</p>
            <p style="margin-bottom: 30px;">SQGATE is entirely free, runs in your browser, and saves your work locally. Try our schematic-based logic simulator today and experience the difference.</p>
            <a href="/home/" style="display: inline-block; background: #8b5cf6; color: #fff; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold;">Launch SQGATE Simulator Now</a>
        </div>'''
    },
    'circuitverse': {
        'name': 'CircuitVerse',
        'title': 'CircuitVerse Alternative - Modern Logic Design | SQGATE',
        'content': '''<div style="background: rgba(12, 15, 28, 0.9); padding: 40px; border-radius: 12px; color: #cbd5e1; max-width: 900px; margin: 40px auto; overflow-y: auto; max-height: 80vh;">
            <h1 style="color: #fff; margin-bottom: 20px;">SQGATE: The Next-Generation Alternative to CircuitVerse</h1>
            <p style="margin-bottom: 15px;"><strong>CircuitVerse</strong> is a popular online digital logic simulator that has helped many students transition from desktop apps to web-based learning. While CircuitVerse provides a good collaborative environment, many users seek an alternative with a more modern interface, faster simulation performance, and deeper educational tools. Enter SQGATE.</p>
            <p style="margin-bottom: 15px;">SQGATE was built from the ground up to provide a premium, fluid user experience. Our rendering engine uses advanced HTML5 Canvas techniques to deliver a visually stunning dark-mode interface with smooth panning, zooming, and wire routing. The user experience feels like a native desktop application, free from the clunkiness often associated with older web apps.</p>
            <p style="margin-bottom: 15px;">Beyond aesthetics, SQGATE packs powerful features that go beyond simple circuit simulation. We integrate a complete Digital Design Suite. This includes a robust Finite State Machine (FSM) designer that automatically generates Verilog code, a Karnaugh Map solver for minimizing expressions up to 6 variables, and the unique Logic Quest puzzle game to test your boolean algebra skills.</p>
            <p style="margin-bottom: 15px;">Privacy and performance are at the core of SQGATE. Unlike CircuitVerse, which emphasizes cloud saving and public projects, SQGATE defaults to local offline storage via IndexedDB. Your circuits remain on your device, ensuring complete privacy and zero latency when saving or loading. You can even install SQGATE as a Progressive Web App (PWA) to use it completely offline on flights or in areas with poor connectivity.</p>
            <p style="margin-bottom: 30px;">If you're looking for a faster, more beautiful, and feature-rich digital logic simulator, SQGATE is the ultimate upgrade. Best of all, it's 100% free.</p>
            <a href="/home/" style="display: inline-block; background: #8b5cf6; color: #fff; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold;">Launch SQGATE Simulator Now</a>
        </div>'''
    },
    'falstad': {
        'name': 'Falstad',
        'title': 'Falstad Circuit Alternative for Digital Logic | SQGATE',
        'content': '''<div style="background: rgba(12, 15, 28, 0.9); padding: 40px; border-radius: 12px; color: #cbd5e1; max-width: 900px; margin: 40px auto; overflow-y: auto; max-height: 80vh;">
            <h1 style="color: #fff; margin-bottom: 20px;">SQGATE vs Falstad: Choosing the Right Circuit Simulator</h1>
            <p style="margin-bottom: 15px;">The <strong>Falstad Circuit Simulator</strong> is an incredible, highly-respected tool for analog electronics. It excels at simulating resistors, capacitors, inductors, op-amps, and seeing current flow in real-time. However, when it comes to designing complex digital logic circuits, Falstad's analog-first approach can become a bottleneck.</p>
            <p style="margin-bottom: 15px;">SQGATE is purpose-built exclusively for digital electronics and boolean logic. Because SQGATE doesn't need to calculate continuous analog voltages (SPICE models), its simulation engine is magnitudes faster for digital networks. You can simulate massive 16-bit CPUs, multiplexer trees, and deep sequential logic without experiencing the slowdowns typical of analog simulators handling digital gates.</p>
            <p style="margin-bottom: 15px;">Our UI is tailored for computer science and digital engineering. Instead of dealing with analog grounds and voltage sources, SQGATE uses pure logical High (1) and Low (0) states. We provide higher-level digital abstractions out of the box, including decoders, encoders, RAM modules, and ROM. You can easily package sub-circuits into Custom ICs, making hierarchical digital design a breeze.</p>
            <p style="margin-bottom: 15px;">Furthermore, SQGATE acts as a bridge to hardware description languages (HDLs). With a single click, you can export your schematic to structural Verilog HDL, a feature impossible in pure analog simulators. We also include a K-Map solver and an FSM designer to round out your digital design education.</p>
            <p style="margin-bottom: 30px;">If you are studying analog circuits, Falstad is king. But if you are studying boolean algebra, computer architecture, or digital logic, SQGATE is the specialized, modern tool you need.</p>
            <a href="/home/" style="display: inline-block; background: #8b5cf6; color: #fff; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold;">Launch SQGATE Simulator Now</a>
        </div>'''
    },
    'logicly': {
        'name': 'Logicly',
        'title': 'Logicly Alternative - Free Logic Gate Simulator | SQGATE',
        'content': '''<div style="background: rgba(12, 15, 28, 0.9); padding: 40px; border-radius: 12px; color: #cbd5e1; max-width: 900px; margin: 40px auto; overflow-y: auto; max-height: 80vh;">
            <h1 style="color: #fff; margin-bottom: 20px;">SQGATE: The Best Free Alternative to Logicly</h1>
            <p style="margin-bottom: 15px;"><strong>Logicly</strong> is a well-known logic circuit simulator that features a clean, intuitive interface. It has been used in classrooms for years to teach boolean logic. However, Logicly is a paid, commercial software product. While it offers a free trial, students and hobbyists on a budget often seek a completely free alternative that doesn't compromise on quality.</p>
            <p style="margin-bottom: 15px;">SQGATE is a 100% free, web-based alternative to Logicly. It offers the same ease-of-use, drag-and-drop interface, and visual interactivity, but without any licensing fees, paywalls, or trial expirations. Because SQGATE runs in the browser, you don't need to install anything on your school or personal computer.</p>
            <p style="margin-bottom: 15px;">Despite being free, SQGATE is arguably more powerful than traditional desktop educational tools. We offer advanced features suitable for university-level computer architecture courses. You can generate custom ICs to encapsulate logic, build complex Finite State Machines (FSMs), and even export your designs to Verilog HDL for FPGA synthesis.</p>
            <p style="margin-bottom: 15px;">Our platform also includes unique learning tools that you won't find in Logicly. The integrated Karnaugh Map (K-Map) solver helps you manually minimize logic equations visually, and our Truth Table generator instantly maps out the behavior of any combinational circuit you draw.</p>
            <p style="margin-bottom: 30px;">Don't let software licensing hold back your learning. Join thousands of students using SQGATE's completely free, offline-capable digital logic simulator.</p>
            <a href="/home/" style="display: inline-block; background: #8b5cf6; color: #fff; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold;">Launch SQGATE Simulator Now</a>
        </div>'''
    }
}

for comp, data in competitors.items():
    filepath = f"{comp}/index.html"
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<meta http-equiv="refresh" content="2; url=/home/">', '')
    
    import re
    html = re.sub(r'<div class="skel-msg">.*?</div>\s*</div>', data['content'] + '</div>', html, flags=re.DOTALL)
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', html, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Competitor pages updated.")
