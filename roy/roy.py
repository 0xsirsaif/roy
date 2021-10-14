import typer

from sys_commands.mount_drive import mount_me
from sys_commands.github import get_github_token

from scripts.imgs_to_file import pngs_to_pdf

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


if __name__ == "__main__":
    app()
