# Theme Definitions
THEMES = {
    "cyberpunk": {
        "border": "bright_magenta",
        "title": "bold italic cyan",
        "header_border": "bold magenta",
        "header_title": "bold white",
        "stack_title": "bold green",
        "stack_border": "green",
        "net_title": "bold cyan",
        "net_border": "cyan",
        "git_title": "bold magenta",
        "git_border": "magenta",
        "hw_title": "bold yellow",
        "hw_border": "yellow",
        "proj_title": "bold blue",
        "proj_border": "blue",
    },
    "matrix": {
        "border": "green",
        "title": "bold green",
        "header_border": "dim green",
        "header_title": "bold white",
        "stack_title": "bold green",
        "stack_border": "green",
        "net_title": "bold green",
        "net_border": "dim green",
        "git_title": "bold green",
        "git_border": "green",
        "hw_title": "bold green",
        "hw_border": "green",
        "proj_title": "bold green",
        "proj_border": "dim green",
    },
    "ocean": {
        "border": "blue",
        "title": "bold italic blue",
        "header_border": "cyan",
        "header_title": "bold white",
        "stack_title": "bold cyan",
        "stack_border": "blue",
        "net_title": "bold blue",
        "net_border": "cyan",
        "git_title": "bold blue",
        "git_border": "blue",
        "hw_title": "bold cyan",
        "hw_border": "cyan",
        "proj_title": "bold blue",
        "proj_border": "blue",
    }
}

def get_theme(name):
    return THEMES.get(name, THEMES["cyberpunk"])
