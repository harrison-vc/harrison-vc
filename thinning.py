import subprocess
import os

def delete_commits():
    # Target: commits between Jan 1 2025 and May 1 2025
    # Get all commit hashes in that range
    result = subprocess.run([
        "git", "log", 
        "--since=2025-01-01", "--until=2025-05-01", 
        "--format=%H"
    ], capture_output=True, text=True)
    
    hashes = result.stdout.strip().split("\n")
    if not hashes or hashes == [""]:
        print("No commits found in range.")
        return

    print(f"Found {len(hashes)} commits in range. Thinning by 60%...")
    
    # We will keep every 3rd commit to thin out the "3000" count significantly
    to_delete = []
    for i, h in enumerate(hashes):
        if i % 3 != 0:
            to_delete.append(h)
            
    print(f"Actually, to be safe and clean, we will do a squashed fill instead.")

# We will use a simpler approach: Revert the whole block and do a 1-commit-per-day fill.
