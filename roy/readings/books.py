# import appdirs
# from cachelib import FileSystemCache

# CACHE_EMPTY_VAL = "NULL"
# CACHE_DIR = appdirs.user_cache_dir("roy")
# CACHE_ENTRY_MAX = 12


# class NewFileSystemCache(FileSystemCache):
#     def __init__(
#         self,
#         cache_dir: str,
#         threshold: int = 500,
#         default_timeout: int = 300,
#         mode: int = 0o600,
#     ):
#         super().__init__(cache_dir, threshold, default_timeout, mode)
#
#     def append(self, key, value):
#         if self.has(key):
#             super().set(key, value)
#         else:
#             super().add(key, value)
#
#         print("id added ???", self.get(key))
#
#         all_keys = self.get("*")
#         if all_keys:
#             new_keys = "".join(k for k in all_keys) + key + ","
#             print("11111", new_keys)
#             super().set("*", new_keys)
#             print("111 all ??", self.get("*"))
#         else:
#             added_key = key + ","
#             print("222222", added_key)
#             super().add("*", added_key)
#             print("222 all ??", self.get("*"))
#         print("id added ???", self.get(key))
#         print("all ???", self.get("*"))
#
#     def remove(self, key):
#         super().delete(key)
#
#         keys = self.get("*").split(",")
#         key_idx = keys.index(key)
#         keys.pop(key_idx)
#         self.set("*", keys)


# cache = NewFileSystemCache(CACHE_DIR, CACHE_ENTRY_MAX, default_timeout=0)

import json


def list_books():
    with open("/media/data/projects/roy/roy/readings/BOOKS.json", "r") as f:
        books = [i for i in json.load(f)]
        print(books)


def add_book(name, location):
    with open("/media/data/projects/roy/roy/readings/BOOKS.json", "r") as f:
        books = [i for i in json.load(f)]

    books.append({name: location})

    with open("/media/data/projects/roy/roy/readings/BOOKS.json", "w") as output_file:
        json.dump(books, output_file)


def remove_book(book_name):
    print(book_name)


def clear_books():
    with open("/media/data/projects/roy/roy/readings/BOOKS.json", "w") as file:
        json.dump([], file)
