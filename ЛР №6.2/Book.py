class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}"

    def __repr__(self):
        return f"Book(id={self.id}, name={self.name}, pages={self.pages})"