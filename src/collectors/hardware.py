import psutil

def get_hardware_info():
    """Collects CPU and RAM usage."""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    
    ram = psutil.virtual_memory()
    ram_total_gb = ram.total / (1024**3)
    ram_used_gb = ram.used / (1024**3)
    ram_percent = ram.percent
    
    return {
        "cpu_percent": cpu_percent,
        "ram_total_gb": f"{ram_total_gb:.1f}",
        "ram_used_gb": f"{ram_used_gb:.1f}",
        "ram_percent": ram_percent
    }
