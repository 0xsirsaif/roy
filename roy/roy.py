from typing import Optional, Tuple
import typer

from console import get_console

from mount_drive import mount_me
from github import get_github_token
from books import PrintAllReads

from imgs_to_file import pngs_to_pdf

app = typer.Typer()


@app.command()
def hello(name: str, job: str):
    typer.echo(f"hello {name}, {job}")


@app.command()
def goodbye(name: str):
    typer.echo(f"Bye {name}!")


@app.command()
def mount(drive: str):
    mount_me(drive)


@app.command()
def github_token():
    typer.echo(get_github_token())


@app.command()
def imgs_to_pdf(src: str, destination: str) -> None:
    pngs_to_pdf(src, destination)


@app.command()
def books():
    all_books = PrintAllReads()
    console = get_console()
    console.print(all_books.print_all_reads())


if __name__ == "__main__":
    app()
