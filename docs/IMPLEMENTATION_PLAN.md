# Future Implementation Plan

## 1. Overview
When adding new features or launching entirely new products under the SQGATE umbrella, follow this core implementation flow to ensure consistency with the existing architecture.

## 2. General Principles
- **No Build Steps:** Features must be written in Vanilla ES6+ and run directly in the browser. Avoid introducing Webpack, Babel, or React.
- **Client-Side Heavy:** All computation (e.g., parsing Verilog, generating truth tables) must run in the browser to maintain zero latency.
- **Styling:** Adhere strictly to the design tokens in `index.html` (e.g., `var(--bg0)`, `var(--t1)`, `var(--acc)`). Do not hardcode HEX colors into inline styles for new components.

## 3. Workflow for New Features
1. **Analyze Requirements:** Read the PRD and TRD. Identify if the feature requires a new standalone page (like `/fsm`) or an addition to the existing simulator.
2. **Draft UI:** Add the HTML structure. Use Flexbox/Grid for layout and maintain the `.tb-btn` / `.tb-btn-text` structures for consistent toolbars.
3. **Logic Implementation:** Add logic strictly modularized via JS closures or minimal objects. 
4. **Data Persistence:** Ensure that any state changes are safely serializable to JSON and saved via the standard `localStorage` mechanism.
5. **Mobile Verification:** Test the view in a 360px portrait window. If the UI cannot function at that width, apply the `#mobile-portrait-overlay` pattern to force landscape usage.
6. **Deploy & SEO:** Ensure any new page has proper `<meta>` and OpenGraph tags mirroring the root SEO setup.
