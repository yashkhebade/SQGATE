# UI/UX Brief

## 1. Design Language
- **Aesthetic:** Modern, sleek, "hacker" dark-mode first. Emphasizes clean lines and glowing elements to simulate electronic circuitry.
- **Color Palette:**
  - **Backgrounds:** Deep dark blues/blacks (`#0f1729`, `#060813`) to reduce eye strain.
  - **Accents/Glows:** Neon blues/purples for active states and brand highlights (`var(--acc)`, `--acc-glow`).
  - **Wires & Logic:** Glowing green (Logic 1) and muted grey/red (Logic 0).
  - **Text:** Slate grays for secondary text (`var(--t2)`), crisp white/light gray for primary text (`var(--t1)`).

## 2. Interaction Model
- **Drag & Drop:** Primary method for placing gates and connecting nodes in the simulator.
- **Toolbar:** Minimalist toolbars with SVG icons (`.tb-btn`). Buttons grow/adapt to content (no fixed 32x32px constraints for text buttons).
- **Feedback:** Hover states use slight brightness adjustments (`filter: brightness(1.15)`) and smooth CSS transitions (`transform: translateY(-1px)`).

## 3. Responsive Strategy
- **Desktop First:** The canvas inherently requires mouse precision.
- **Mobile Constraints:** Users on portrait screens see an overlay forcing them into landscape (`#mobile-portrait-overlay`). Text buttons adapt to avoid squishing.
