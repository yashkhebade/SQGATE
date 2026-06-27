# Technical Requirement Document (TRD)

## 1. System Architecture
- **Frontend Stack:** Pure Vanilla HTML5, CSS3, and JavaScript (ES6+). No heavy frameworks (React/Vue/Angular) to ensure maximum performance and absolute zero build steps for local development.
- **State Management:** Uses browser `localStorage` to persist user sessions, projects, and Pro status (`CU` variable).
- **Hosting:** Static hosting (e.g., GitHub Pages, Vercel, Netlify) served over HTTPS.

## 2. Telemetry & Analytics
- **Backend Service:** Supabase (PostgreSQL).
- **Purpose:** Collects anonymous structural circuit data (gates, wires, coordinates) for ML model training.
- **Privacy Rule:** Strictly bypassed if the user logs in with an email address. Guests trigger telemetry.

## 3. UI/UX Constraints
- **Device Support:** Highly optimized for desktop (landscape). Mobile users receive a "Force Landscape" overlay as the drag-and-drop workspace is difficult to navigate on narrow viewports.
- **Performance:** Rendering engine uses standard DOM manipulation (or Canvas where applicable) optimized for 60fps interaction during simulation.

## 4. Dependencies
- Minimal external dependencies.
- **Payment Gateway:** Lemon Squeezy API for Pro upgrades and checkout flows.
- **Icons:** SVG icons embedded inline or via lightweight assets.
