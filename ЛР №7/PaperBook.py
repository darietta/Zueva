from Book import Book


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.__name = name
        self.__author = author
        self.__pages = pages

    def set_page(self, pages):
        if 0 < pages < float("inf"):
            self.__pages = pages
        else:
            print("Недопустимое количество страниц")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
