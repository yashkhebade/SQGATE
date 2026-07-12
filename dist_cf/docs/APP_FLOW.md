# Application Flow

## 1. Landing and Redirection
- User visits `https://sqgate.online/`
- Root `index.html` serves SEO metadata and automatically redirects via JavaScript/Meta Refresh to `/home`.

## 2. Dashboard (`/home`)
- **Hero Section:** Introduction, features, and quick links to open workspaces.
- **Top Navigation:** Contains Links to Tools, User Profile (Guest or Logged in via email), and the "Get SQGATE Pro" upgrade button.
- **Project Selection (Guest Session):** Users can start immediately as a guest. Telemetry will run in the background.

## 3. Core Applications (Tools)
From the dashboard, users launch specific modules:
1. **Circuit Simulator (`/circuit-simulator`):** Primary drag-and-drop workspace for wiring gates and testing logic.
2. **FSM Designer (`/fsm`):** Visual state machine editor with Verilog export functionality.
3. **K-Map Solver (`/k-map`):** Tool for simplifying Boolean expressions up to 6 variables.
4. **Logic Puzzles (`/puzzle`):** Interactive challenges to test understanding.

## 4. Mobile Handling
- If a user accesses any workspace on a mobile device (portrait mode), a full-screen overlay triggers: `Please Rotate Device`.
- Users must force landscape or auto-rotate to gain access to the UI, as the tools require horizontal screen real estate.
