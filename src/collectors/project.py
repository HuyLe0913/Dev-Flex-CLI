import os

def get_project_stats():
    """Scans current directory/SRC for basic stats."""
    # Count files by extension
    ext_counts = {}
    total_files = 0
    total_size = 0
    
    exclude_dirs = {'.git', 'venv', '__pycache__', 'node_modules', '.idea', '.vscode'}
    
    for root, dirs, files in os.walk("."):
        # Modify dirs in-place to exclude unwanted
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for f in files:
            total_files += 1
            try:
                total_size += os.path.getsize(os.path.join(root, f))
            except:
                pass
            
            ext = os.path.splitext(f)[1].lower()
            if not ext:
                ext = "no-ext"
            
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
            
    # Top 5 extensions
    sorted_exts = sorted(ext_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Convert size
    if total_size > 1024**3:
        size_str = f"{total_size / (1024**3):.2f} GB"
    elif total_size > 1024**2:
        size_str = f"{total_size / (1024**2):.2f} MB"
    else:
        size_str = f"{total_size / 1024:.2f} KB"
        
    return {
        "total_files": total_files,
        "total_size": size_str,
        "top_exts": sorted_exts
    }
