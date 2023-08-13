import logging

import typer
from dotenv import load_dotenv
from rich.console import Console

from .toggl_api import list_clients, list_projects, time_entries, who_am_i

load_dotenv()
console = Console()
app = typer.Typer()


logging.basicConfig(
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)


@app.command()
def hello(name: str):
    print(f"Hello, {name}!")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye, Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def me():
    result = who_am_i()
    console.print(result)


@app.command()
def time():
    result = time_entries()
    # console.print(result)
    print(f"Got {len(result)} entries")
    console.print(result)


@app.command()
def projects():
    result = list_projects()
    console.print(result)


@app.command()
def clients():
    result = list_clients()
    console.print(result)


if __name__ == "__main__":
    app()
