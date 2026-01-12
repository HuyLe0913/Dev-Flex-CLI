from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box
from rich.progress import BarColumn, Progress, TextColumn

def create_header(sys_info, theme):
    """Creates the header grid with system info."""
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    
    # System Info Row
    os_info = f"[{theme['header_title']}]🖥️  {sys_info['os']}[/]"
    kernel_info = f"[dim]Kernel: {sys_info['kernel']}[/]"
    uptime_info = f"[bold green]⏱️  {sys_info['uptime']}[/]"
    shell_info = f"[bold yellow]🐚 {sys_info['shell']}[/]"
    
    grid.add_row(f"{os_info}  •  {kernel_info}  •  {uptime_info}  •  {shell_info}")
    return Panel(grid, style=theme['header_border'], title=f"[{theme['header_title']}]SYS.INFO[/]", title_align="left", padding=(1, 2))

def create_hardware_panel(hw_info, theme):
    """Creates a Hardware Monitor panel."""
    # Create progress bars for CPU and RAM
    
    # CPU Bar
    cpu_bar = Progress(
        TextColumn("[bold]CPU[/]"),
        BarColumn(bar_width=None, style="dim white", complete_style="red" if hw_info['cpu_percent'] > 80 else "green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        expand=True
    )
    cpu_task = cpu_bar.add_task("CPU", total=100, completed=hw_info['cpu_percent'])
    
    # RAM Bar
    ram_bar = Progress(
        TextColumn("[bold]RAM[/]"),
        BarColumn(bar_width=None, style="dim white", complete_style="yellow" if hw_info['ram_percent'] > 80 else "blue"),
        TextColumn("{task.completed}/{task.total} GB"),
        expand=True
    )
    ram_task = ram_bar.add_task("RAM", total=float(hw_info['ram_total_gb']), completed=float(hw_info['ram_used_gb']))

    # Layout
    grid = Table.grid(expand=True, padding=(0, 2))
    grid.add_column(ratio=1)
    grid.add_row(cpu_bar)
    grid.add_row(ram_bar)

    return Panel(grid, title=f"[{theme['hw_title']}]HARDWARE[/]", border_style=theme['hw_border'])

def create_project_panel(proj_info, theme):
    """Creates Project Stats panel."""
    grid = Table.grid(expand=True, padding=(0, 1))
    grid.add_column(style="bold white")
    grid.add_column(justify="right", style="dim white")
    
    grid.add_row(f"📂 Total Files", str(proj_info['total_files']))
    grid.add_row(f"💾 Total Size", proj_info['total_size'])
    grid.add_row(" ", " ")
    
    for ext, count in proj_info['top_exts']:
        grid.add_row(f"  {ext}", str(count))

    return Panel(grid, title=f"[{theme['proj_title']}]PROJECT SCAN[/]", border_style=theme['proj_border'])

def create_stack_table(stack_info, theme):
    """Creates the Dev Stack table."""
    table = Table(box=box.SIMPLE, expand=True, show_header=False, padding=(0, 2))
    table.add_column("Tool", style="bold cyan")
    table.add_column("Version", style="bold white")

    icons = {
        "Python": "🐍",
        "Node.js": "🟢",
        "Go": "🐹",
        "Rust": "🦀",
        "Docker": "🐳",
    }

    for tool, version in stack_info.items():
        icon = icons.get(tool, "🔧")
        if version:
            table.add_row(f"{icon} {tool}", version)
        else:
            table.add_row(f"{icon} {tool}", "[dim red]Not Installed[/]")
    
    return Panel(table, title=f"[{theme['stack_title']}]DEV STACK[/]", border_style=theme['stack_border'])

def create_network_panel(net_info, speedtest_info, theme):
    """Creates Network info panel."""
    grid = Table.grid(expand=True, padding=(0, 1))
    grid.add_column(style="bold cyan")
    grid.add_column(justify="right", style="bold white")

    grid.add_row("🏠 Local IP", net_info['local_ip'])
    if net_info['public_ip']:
         grid.add_row("🌐 Public IP", net_info['public_ip'])
    
    if speedtest_info:
        grid.add_row(" ", " ")
        grid.add_row("⚡ Ping", speedtest_info['ping'])
        grid.add_row("⏬ Download", speedtest_info['download'])
    
    return Panel(grid, title=f"[{theme['net_title']}]NETWORK[/]", border_style=theme['net_border'])

def create_git_panel(git_info, theme):
    """Creates Git info panel if available."""
    if not git_info:
         return Panel(Align.center("[dim italic]No Git Repository Detected[/]"), title=f"[{theme['git_title']}]GIT CONTEXT[/]", border_style="dim " + theme['git_border'])

    grid = Table.grid(expand=True, padding=(0, 1))
    grid.add_column(style="bold magenta")
    grid.add_column(justify="right", style="bold white")

    grid.add_row("🎋 Branch", git_info['branch'])
    grid.add_row("🔗 Commit", git_info['commit'][0:7])
    
    status_color = "green" if git_info['status'] == "Clean" else "red"
    grid.add_row("📝 Status", f"[{status_color}]{git_info['status']}[/]")

    return Panel(grid, title=f"[{theme['git_title']}]GIT CONTEXT[/]", border_style=theme['git_border'])
