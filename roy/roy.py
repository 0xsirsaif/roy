import typing
import subprocess
import typer

from sys_commands.mount_drive import mount_me
from sys_commands.github import get_github_token

app = typer.Typer()


@app.command()
def hello(name: str, job: str):
    typer.echo(F"hello {name}, {job}")


@app.command()
def goodbye(name: str):
    typer.echo(F"Bye {name}!")


@app.command()
def mount(drive: str):
    mount_me(drive)


@app.command()
def github_token():
    typer.echo(get_github_token())


if __name__ == "__main__":
    app()
