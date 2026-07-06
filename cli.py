from rich.console import Console
from rich.panel import Panel

from src.config import load_config
from src.logger import logger

console = Console()


def start_application():

    config = load_config()

    console.print(
        Panel.fit(
            "[bold cyan]LLM TeacherEval[/bold cyan]\n"
            "Educational AI Benchmark Framework"
        )
    )

    logger.info("Application started")

    console.print()

    console.print("[green]Available Models[/green]")

    console.print()

    for model in config["benchmark"]["models"]:

        console.print(f" • {model}")

    console.print()

    console.print("[yellow]Framework initialized successfully.[/yellow]")