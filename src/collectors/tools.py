import shutil
import subprocess
import platform

def get_tool_version(command, args):
    """Runs a command to get a version string."""
    if not shutil.which(command):
        return None
    try:
        # Prevent popup window on Windows
        startupinfo = None
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        result = subprocess.run(
            [command] + args, 
            capture_output=True, 
            text=True, 
            timeout=2, 
            startupinfo=startupinfo
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Timeout"
    except Exception:
        return "Error"
    return None

def get_dev_stack():
    """Checks versions of common dev tools."""
    tools = {
        "Python": ("python", ["--version"]),
        "Node.js": ("node", ["--version"]),
        "Go": ("go", ["version"]),
        "Rust": ("rustc", ["--version"]),
        "Docker": ("docker", ["--version"]),
    }
    
    results = {}
    for name, (cmd, args) in tools.items():
        raw_version = get_tool_version(cmd, args)
        if raw_version:
            if name == "Python":
                version = raw_version.split()[-1]
            elif name == "Go":
                parts = raw_version.split()
                version = parts[2] if len(parts) > 2 else raw_version
            elif name == "Docker":
                version = raw_version.split(',')[0].replace("Docker version", "").strip()
            else:
                version = raw_version
            results[name] = version
        else:
            results[name] = None
    return results
