# Backup Instructions
- The user maintains a backup of this project on their E: drive at `E:\sqgate`.
- After every 2-3 significant updates or code changes, automatically copy the entire workspace to `E:\sqgate` to keep the backup synchronized. 
- You can use PowerShell for this: `Copy-Item -Path ".\*" -Destination "E:\sqgate" -Recurse -Force`

# Stable Backup Instructions
- The user maintains a secondary backup for *stable* versions on their D: drive at `D:\sqgatebackup`.
- Do NOT automatically sync this location. Only back up to `D:\sqgatebackup` if the user explicitly requests it.
- Additionally, every 5-10 interactions, proactively ask the user: "Would you like me to store a stable backup to D:\sqgatebackup?". If they say yes, execute the backup. If they say no, do nothing.
# Backup Instructions
- The user maintains a backup of this project on their E: drive at `E:\sqgate`.
- After every 2-3 significant updates or code changes, automatically copy the entire workspace to `E:\sqgate` to keep the backup synchronized. 
- You can use PowerShell for this: `Copy-Item -Path ".\*" -Destination "E:\sqgate" -Recurse -Force`

# Stable Backup Instructions
- The user maintains a secondary backup for *stable* versions on their D: drive at `D:\sqgatebackup`.
- Do NOT automatically sync this location. Only back up to `D:\sqgatebackup` if the user explicitly requests it.
- Additionally, every 5-10 interactions, proactively ask the user: "Would you like me to store a stable backup to D:\sqgatebackup?". If they say yes, execute the backup. If they say no, do nothing.
- You can use PowerShell for this: `Copy-Item -Path ".\*" -Destination "D:\sqgatebackup" -Recurse -Force`

# Documentation First Policy
- Before planning or implementing any new feature, product, or architectural change, you MUST read the documents in the `docs/` directory (specifically `PRD.md`, `TRD.md`, `APP_FLOW.md`, `UI_UX_BRIEF.md`, and `IMPLEMENTATION_PLAN.md`).
- Ensure all new code adheres to the constraints defined in these documents (e.g., pure Vanilla JS, no build steps, consistent typography, client-side execution).

# Mandatory SEO, Tracking, and Monetization Tags
- Whenever creating or generating a new blog post or webpage, it MUST include comprehensive SEO meta tags, Google Analytics tracking code, and Google AdSense tags.
- This includes `<title>`, `<meta name="description">`, `<meta name="keywords">`, canonical links, and Open Graph (`og:`) tags.
- You must also inject the `<script>` tags for Google AdSense and Google Analytics (gtag.js) into the `<head>` or body as appropriate.
- Do not publish or save any new content pages without ensuring these tags are populated.

# Automated User Feedback Monitoring
- The user collects bug reports and feature requests via a Google Form linked to a Google Sheet.
- The live CSV export URL for these responses is: `https://docs.google.com/spreadsheets/d/1oIKIRt-ZeGUSKnFN7F43dcOndOFqby44k79mPvyqcr4/export?format=csv`
- You MUST proactively keep an eye on this feedback. Whenever you have downtime or when explicitly asked, use `read_url_content` to fetch this CSV.
- Compare the timestamp of the latest rows against the previously solved issues.
- If there is a new, unresolved request, automatically analyze it and propose/implement a solution strictly adhering to the project's constitution (Pure Vanilla JS, no build steps, client-side execution, consistent UI/UX).
- After fixing an issue from the form, document that it was solved so it is not repeated.

# Dynamic Blog Images Policy
- Do NOT use generic or repeated placeholder images (like the default green circuit) when creating or updating blog posts.
- Every time you create a new blog post, you MUST use the `generate_image` tool to create a visually stunning, highly relevant, and unique image specific to that post's topic (e.g., a state machine diagram for FSM posts, or a dynamic CMOS visualization for logic gates).
- Ensure the generated image is properly saved and referenced in both the blog index page and the post's `<meta property="og:image">` tags.

# SQGATE Architectural Constraints & UI Modification Policy
- **Meticulous HTML Structure**: The core application (`home/index.html`) is a massive monolithic file without a build step or linter. When modifying modals, toolbars, or UI overlays, you MUST meticulously verify that all `<div>` tags are perfectly closed. A single unclosed tag will cause cascading DOM failures, swallowing the rest of the application into hidden containers.
- **Event Binding Preference**: When adding new buttons or UI interactions, ALWAYS prefer direct inline event handlers (e.g., `<button onclick="startTour()">`) rather than deferred Javascript event listeners attached via `DOMContentLoaded`. This ensures rock-solid execution in the monolithic script environment and plays nicely with the aggressive Service Worker cache.
- **Service Worker Cache Busting**: Whenever you make structural HTML changes or add inline Javascript to a core file, manually bump the `CACHE_NAME` version string in `sw.js` to force clients to bypass their aggressive local cache.

# Verilog/VHDL Code Generation Rules
- **Multi-bit Bus Widths**: When updating the `genVerilog()` or `genVHDL()` exporters, never default all internal nets to 1-bit wires. You must analyze the source gate type to declare the correct bit width (e.g., `wire [7:0]` or `STD_LOGIC_VECTOR(7 downto 0)`) for components that output buses, such as `count8`, `shift8`, `alu8`, `rom8`, `ram8`, and bus splitters.
- **Endianness & Array Mapping**: Ensure that splitters (`split8`, `split4`) and mergers (`merge8`, `merge4`) map their outputs array-index for array-index to match the MSB-first evaluation logic of the Javascript simulation engine.
