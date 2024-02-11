from Book import Book


class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        self.__name = name
        self.__author = author
        self.__duration = duration

    def set_duration (self, duration):
        if 0 < duration < float("inf"):
            self.__duration = duration
        else:
            print("Недопустимая длительность")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
