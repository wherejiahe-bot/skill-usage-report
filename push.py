#!/usr/bin/env python3
"""Push updated data to GitHub repo wherejiahe-bot/skill-usage-report"""
import subprocess, os, sys

REPO_URL = "git@github.com:wherejiahe-bot/skill-usage-report.git"
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

def run(cmd, cwd=None):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd or LOCAL_DIR)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode

def main():
    print(f"Working dir: {LOCAL_DIR}")

    # 1. Add files
    rc = run("git add -A")
    if rc != 0:
        print("git add failed, trying init...")
        run("git init")
        run("git add -A")

    # 2. Commit if changed
    rc = run("git diff --cached --quiet")
    if rc != 0:  # files changed
        run('git commit -m "chore: update skill usage report 2026-06-17"')
    else:
        print("No changes to commit")
        return

    # 3. Remote setup
    run("git remote -v")

    # 4. Pull first to avoid conflicts
    rc = run("git pull origin main --rebase", cwd=LOCAL_DIR)
    if rc != 0:
        print("Pull may have failed, continuing...")

    # 5. Push
    rc = run("git push origin main")
    if rc == 0:
        print("\n✅ Push successful!")
    else:
        print(f"\n❌ Push failed (rc={rc})")
        # Try alternative remote
        run("git remote add github " + REPO_URL if "github" not in run("git remote", cwd=LOCAL_DIR).stdout else "")
        run("git push github main")

if __name__ == "__main__":
    main()
