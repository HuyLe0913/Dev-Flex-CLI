import platform
import distro
import os
import psutil
import datetime

def get_system_info():
    """Collects OS, Kernel, Uptime, and Shell info."""
    os_name = "Unknown"
    
    # Improved Windows detection
    if platform.system() == "Windows":
        try:
            release = platform.release()
            
            edition = platform.win32_edition() if hasattr(platform, 'win32_edition') else ""
            os_name = f"Windows {release} {edition}".strip()
        except:
            os_name = f"Windows {platform.release()}"
    else:
        try:
            os_name = f"{distro.name(pretty=True)} {distro.version()}"
        except:
            os_name = f"{platform.system()} {platform.release()}"

    kernel = platform.release()
    
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    uptime_str = str(uptime).split('.')[0] # Remove microseconds

    shell = os.environ.get('SHELL') or os.environ.get('COMSPEC')
    if shell:
        shell = os.path.basename(shell)
    else:
        shell = "Unknown"

    return {
        "os": os_name,
        "kernel": kernel,
        "uptime": uptime_str,
        "shell": shell
    }
