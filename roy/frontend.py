from rich.table import Table


def salah_in_table(title, columns_head, data):
    table = Table(title=title)

    for col in columns_head:
        table.add_column(col, style="cyan", no_wrap=True)

    for k, v in data.items():
        table.add_row(k, v)

    return table