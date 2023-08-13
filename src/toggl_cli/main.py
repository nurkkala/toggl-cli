import typer
from dotenv import load_dotenv
from rich.console import Console

from toggl_cli.toggl_api import who_am_i

load_dotenv()
console = Console()
app = typer.Typer()


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


if __name__ == "__main__":
    app()
