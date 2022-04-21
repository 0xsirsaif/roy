from typing import Optional
from rich.console import Console

console: Optional[Console] = None


def get_console():
    global console

    if not console:
        console = Console()
    return console
