#!/usr/bin/env python3
"""Push updated skill-usage-report to GitHub."""
import subprocess
import sys

def run(cmd):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode

def main():
    print("Working directory:", __import__('os').getcwd())
    # Add all files
    run("git add -A")
    # Commit if there are changes
    rc = run("git diff --cached --quiet")
    if rc != 0:
        from datetime import date
        today = date.today().isoformat()
        run(f'git commit -m "chore: update skill usage report {today}"')
        run("git push origin master")
    else:
        print("No changes to commit.")

if __name__ == "__main__":
    main()
