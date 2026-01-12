from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .themes import get_theme
from .panels import (
    create_header, create_hardware_panel, create_stack_table,
    create_network_panel, create_git_panel, create_project_panel
)

console = Console()

def render_dashboard(data, theme_name="cyberpunk"):
    """Renders the full dashboard."""
    theme = get_theme(theme_name)
    
    # Header
    header = create_header(data['system'], theme)
    
    # Hardware (Row 1)
    hw_panel = create_hardware_panel(data['hardware'], theme)
    
    # Row 2 Content
    stack_panel = create_stack_table(data['stack'], theme)
    
    network_panel = create_network_panel(data['network'], data['speedtest'], theme)
    git_panel = create_git_panel(data['git'], theme)
    project_panel = create_project_panel(data['project'], theme)

    # Left Column
    left_col = Table.grid(expand=True)
    left_col.add_column()
    left_col.add_row(stack_panel)
    left_col.add_row(project_panel)

    # Right Column
    right_col = Table.grid(expand=True)
    right_col.add_column()
    right_col.add_row(network_panel)
    right_col.add_row(git_panel)

    # Main Grid for Row 2
    row2_grid = Table.grid(expand=True, padding=(0, 1))
    row2_grid.add_column(ratio=1) # Left
    row2_grid.add_column(ratio=1) # Right
    row2_grid.add_row(left_col, right_col)

    final_grid = Table.grid(expand=True, padding=(0, 0))
    final_grid.add_column()
    final_grid.add_row(header)
    final_grid.add_row(hw_panel)
    final_grid.add_row(row2_grid)

    console.print(Panel(final_grid, title=f"[{theme['title']}]DEV-FLEX[/]", border_style=theme['border']))
