import shutil
import subprocess

def get_git_info():
    """Gets current git context if in a repo."""
    if not shutil.which("git"):
        return None
    
    # Check if inside a repo
    try:
        subprocess.check_call(["git", "rev-parse", "--is-inside-work-tree"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        return None # Not a git repo

    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
        
        # Check status
        status_output = subprocess.check_output(["git", "status", "--porcelain"], text=True).strip()
        status = "Dirty" if status_output else "Clean"
        
        return {"branch": branch, "commit": commit, "status": status}
    except:
        return None
