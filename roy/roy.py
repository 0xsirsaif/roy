from typing import Optional, Tuple
import typer

from sys_commands.mount_drive import mount_me
from sys_commands.github import get_github_token

from scripts.imgs_to_file import pngs_to_pdf

from readings.books import list_books, add_book, remove_book, clear_books, open_book


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
def books(
    add: Tuple[str, str] = typer.Option((None, None)),
    rm: Optional[str] = typer.Option(None),
    clear: Optional[str] = typer.Option(None),
    book: Optional[str] = typer.Option(None),
):
    book_name, book_location = add
    if book_name:
        add_book(book_name, book_location)
    if rm:
        remove_book(rm)
    if clear:
        clear_books()
    if book:
        open_book(book)

    typer.echo(list_books())


if __name__ == "__main__":
    app()
