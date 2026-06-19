#!/usr/bin/env python3
"""Push updated skill-usage-report to GitHub."""
import subprocess, sys, os

def run(cmd):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode

def ensure_ssh_remote():
    """Switch remote from HTTPS to SSH if needed (GitHub HTTPS is blocked in China)."""
    rc = run("git remote get-url origin")
    if rc != 0:
        print("WARN: no remote 'origin' configured")
        return False
    # get-url outputs to stdout — check the last captured url by re-running with capture
    result = subprocess.run(
        "git remote get-url origin", shell=True, capture_output=True, text=True
    )
    url = result.stdout.strip()
    if url.startswith("https://github.com/"):
        ssh_url = url.replace(
            "https://github.com/", "git@github.com:"
        ).replace(
            ".git", ".git", 1
        )
        # strip embedded credentials if any
        if "@" in ssh_url and ssh_url.startswith("https://"):
            ssh_url = f"git@github.com:{'/'.join(url.split('/')[3:])}"
            if not ssh_url.endswith(".git"):
                ssh_url += ".git"
        print(f"Switching remote from HTTPS to SSH: {ssh_url}")
        subprocess.run(f'git remote set-url origin "{ssh_url}"', shell=True)
    return True

def main():
    print("Working directory:", os.getcwd())
    ensure_ssh_remote()
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
