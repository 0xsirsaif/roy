import json
import subprocess


def open_book(book):
    with open("/media/data/projects/roy/roy/readings/Books.json", "r") as f:
        book_location = [
            list(j.values())[0] for i, j in enumerate(json.load(f)) if i == int(book)
        ]

    try:
        subprocess.run(["xdg-open", book_location[0]])
    except IndexError:
        print("No location")


def list_books():
    with open("/media/data/projects/roy/roy/readings/Books.json", "r") as f:
        books = [(i, list(j.keys())) for i, j in enumerate(json.load(f))]
        return books


def add_book(name, location):
    with open("/media/data/projects/roy/roy/readings/Books.json", "r") as f:
        books = [i for i in json.load(f)]

    books.append({name: location})

    with open("/media/data/projects/roy/roy/readings/Books.json", "w") as output_file:
        json.dump(books, output_file)


def remove_book(book_name):
    print(book_name)


def clear_books():
    with open("/media/data/projects/roy/roy/readings/Books.json", "w") as file:
        json.dump([], file)
