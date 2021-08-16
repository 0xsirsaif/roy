import typing
import typer


app = typer.Typer()


@app.command()
def hello(name: str, job: str):
    typer.echo(F"hello {name}, {job}")


@app.command()
def goodbye(name: str):
    typer.echo(F"Bye {name}!")


if __name__ == "__main__":
    app()
