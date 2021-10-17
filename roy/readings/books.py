import appdirs
from cachelib import FileSystemCache

CACHE_EMPTY_VAL = "NULL"
CACHE_DIR = appdirs.user_cache_dir("roy")
CACHE_ENTRY_MAX = 12


class NewFileSystemCache(FileSystemCache):
    def __init__(
        self,
        cache_dir: str,
        threshold: int = 500,
        default_timeout: int = 300,
        mode: int = 0o600,
    ):
        super().__init__(cache_dir, threshold, default_timeout, mode)

    def append(self, key, value):
        super().add(key, value)
        all_keys = self.get("*")
        if all_keys:
            new_keys = "".join(k for k in all_keys) + key + ","
            super().set("*", new_keys)
        else:
            added_key = key + ","
            super().add("*", added_key)

    def remove(self, key):
        super().delete(key)

        keys = self.get("*").split(",")
        key_idx = keys.index(key)
        keys.pop(key_idx)
        self.set("*", keys)


cache = NewFileSystemCache(CACHE_DIR, CACHE_ENTRY_MAX, default_timeout=0)


def list_books():
    books = cache.get("*")
    all_books = [cache.get(key) for key in books[:-1]] if books else "No Books"
    return all_books


def add_book(name, location):
    cache.append(name, location)


def remove_book(book_name):
    cache.remove(book_name)


def clear_books():
    cache.clear()
