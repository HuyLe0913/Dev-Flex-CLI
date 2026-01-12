from .system import get_system_info
from .hardware import get_hardware_info
from .network import get_network_info, get_speedtest
from .tools import get_dev_stack
from .git import get_git_info
from .project import get_project_stats

def collect_all(public_ip=False, do_speedtest=False):
    data = {
        "system": get_system_info(),
        "hardware": get_hardware_info(),
        "stack": get_dev_stack(),
        "network": get_network_info(public_ip),
        "git": get_git_info(),
        "project": get_project_stats(),
        "speedtest": None
    }
    
    if do_speedtest:
        data["speedtest"] = get_speedtest()
        
    return data
