# SQGATE User Feedback Issues Solved

This document tracks issues reported in the Google Forms feedback sheet that have been successfully resolved, as mandated by the project constitution.

| Date Reported | Name | Type | Issue Description | Resolution Date | Resolution Details |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 27/06/2026 | harsh | Update | "text is very small can you make it little big and the font can be better on home page and everywhere." | 08/07/2026 | Overhauled UI with modern Inter/Outfit fonts, improved base font sizing, and implemented a Light Theme. |
| 27/06/2026 | Geton Gaming | Bug | "verilog code for cnt is wrong" | 08/07/2026 | Fixed bit-width handling and code generation logic in `genVerilog()` for counters and splitters. |
| 27/06/2026 | Yash | Bug | "Mobile UI is not optimized and feels cramped/unusable... \n Appears at Top of FSM Designer" | 08/07/2026 | Removed stray text nodes causing `\n` bug in FSM and Puzzle modules. Added responsive media query (max-width: 768px) to collapse sidebars and increase touch targets. |
| 30/06/2026 | . | Bug | "No auto rotate on mobile like it use to be before" | 09/07/2026 | Reintroduced CSS `@media screen and (orientation: portrait)` to automatically rotate the canvas 90 degrees when holding phone in portrait mode, fallback for OS orientation lock. |
