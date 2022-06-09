from typing import List, Tuple

from rich.table import Table


def table_view(title: str, columns: List, rows: List[Tuple]):
    table = Table(title=title)

    for col in columns:
        table.add_column(col, style="cyan", no_wrap=True)

    for row in rows:
        table.add_row(*row)

    return table
