import csv
import json
import os
import requests
import subprocess
from io import StringIO

CSV_URL = "https://docs.google.com/spreadsheets/d/1oIKIRt-ZeGUSKnFN7F43dcOndOFqby44k79mPvyqcr4/export?format=csv"
STATE_FILE = "backend/processed_feedback.json"

CONSTITUTION = """
SQGATE FEEDBACK AUTOMATION CONSTITUTION
Version 1.0

Rules are evaluated top-down - higher rank always wins.

RANK 1 - SAFETY, LEGAL & COMMERCIAL INTEGRITY [Hard Block]
Any request to remove ToS, Privacy Policy, payments, or ads.

RANK 2 - DESTRUCTIVE OR IRREVERSIBLE ACTIONS [Hard Block]
Any request to drop tables, delete user data, wipe projects, or remove git history.

RANK 3 - UNDERSPECIFIED OR AMBIGUOUS [Soft Reject]
Vague feedback like 'make it better' or 'it doesn't work' with no details.

RANK 4 - MAJOR ARCHITECTURAL OR SCOPE CREEP [Soft Reject]
Requests to add entire new apps, heavy frameworks, or rip out core vanilla JS.

RANK 5 - UI, CSS & VISUAL FIXES [Auto-Implement]
Font sizes, colors, margins, typos, dark mode toggles.

RANK 6 - BUG FIX IN EXISTING FEATURE [Auto-Implement]
Logic gate simulation bugs, Verilog/VHDL export issues, layout overflow.

RANK 7 - MINOR FEATURE ENHANCEMENT [Auto-Implement]
Adding a new shortcut, a new logic gate primitive (if specified), or simple export format.

RANK 8 - MODERATE FEATURE WORK [Review Queue]
Requires 2+ hours or adding a new system (like a new solver).

RANK 9 - EVERYTHING ELSE [Review Queue]

INSTRUCTIONS: 
You are an autonomous agent processing the feedback below. 
If the feedback falls under Rank 5, 6, or 7, implement the necessary code changes directly in the codebase and save the files.
If the feedback falls under Rank 1, 2, 3, 4, 8, or 9, DO NOT MAKE ANY CODE CHANGES. Just exit.
"""

def main():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                processed = json.load(f)
            except:
                processed = {}
    else:
        processed = {}

    response = requests.get(CSV_URL)
    response.raise_for_status()
    
    csv_text = response.text
    reader = csv.DictReader(StringIO(csv_text))
    
    new_entries = False
    
    for row in reader:
        # Use a combination of Timestamp and Name as a unique key
        timestamp = row.get("Timestamp", "")
        name = row.get("Name", "")
        key = f"{timestamp}_{name}"
        
        if not key or key in processed:
            continue
            
        print(f"Processing new feedback from {name}: {row.get('Subject')}")
        
        feedback_text = f"User Name: {name}\nSubject: {row.get('Subject')}\nDescription: {row.get('Description of Issue or Request')}"
        prompt = CONSTITUTION + "\n\nFEEDBACK:\n" + feedback_text
        
        # Run aider
        try:
            subprocess.run([
                "aider",
                "--message", prompt,
                "--auto-commits",
                "--yes-always"
            ], check=True)
        except Exception as e:
            print(f"Aider encountered an error: {e}")
            
        processed[key] = True
        new_entries = True
        
    if new_entries:
        with open(STATE_FILE, "w") as f:
            json.dump(processed, f, indent=2)
        print("Updated state file.")

if __name__ == "__main__":
    main()
