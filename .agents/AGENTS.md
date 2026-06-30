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
