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
