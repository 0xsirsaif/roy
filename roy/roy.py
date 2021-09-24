import typing
import subprocess
import typer

from sys_commands.mount_drive import mount_me

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


if __name__ == "__main__":
    app()
