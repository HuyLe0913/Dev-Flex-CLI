import typer
from rich.console import Console
from src.collectors import collect_all
from src.ui import render_dashboard

app = typer.Typer()
console = Console()

@app.command()
def main(
    public: bool = typer.Option(False, "--public", help="Fetch public IP address"),
    speedtest: bool = typer.Option(False, "--speedtest", help="Run network speedtest (slow)"),
    theme: str = typer.Option("cyberpunk", "--theme", help="Theme: cyberpunk, matrix, ocean")
):
    """
    Check system info and dev stack versions in style.
    """
    with console.status("[bold green]Collecting system info...[/]", spinner="dots"):
        data = collect_all(public_ip=public, do_speedtest=speedtest)
    
    render_dashboard(data, theme_name=theme)

if __name__ == "__main__":
    app()

