import json
from rich.table import Table


class PrintAllReads:
    with open("/media/data/projects/roy/roy/Books.json") as json_file:
        all_books = json.load(json_file)

    def print_all_reads(self):
        table = Table(title="All Reads")

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Author", style="magenta")
        table.add_column("Progress", justify="left", style="green")

        for n in self.all_books:
            book = self.all_books[n]
            name, author, progress = book["name"], book["Author"], str(book["Progress"])

            table.add_row(name, author, progress)

        return table
