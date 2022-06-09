from typing import Optional, Tuple
import typer
import requests
import json

from console import get_console

from mount_drive import mount_me
from github import get_github_token
from frontend import table_view

from imgs_to_file import pngs_to_pdf

app = typer.Typer()
console = get_console()


@app.command()
def imgs_to_pdf(src: str, destination: str) -> None:
    pngs_to_pdf(src, destination)


@app.command()
def books():
    with open("/media/data/open-source/roy/roy/Books.json") as json_file:
        all_books = json.load(json_file)

    data_to_print = [tuple(book.values()) for book in all_books.values()]
    console.print(table_view("Books", ["Name", "Author", "Progress"], data_to_print))


@app.command()
def salah_time() -> Optional[str]:
    _url_str = "https://dailyprayer.abdulrcs.repl.co/api/egypt"
    response = requests.get(_url_str).json()["today"]

    data_to_print = [(k, v) for k, v in response.items()]
    console.print(table_view("SALAH TIME", ["Salah", "Time"], data_to_print))
    return


if __name__ == "__main__":
    app()
