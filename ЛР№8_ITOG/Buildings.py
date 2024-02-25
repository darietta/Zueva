# Базовый/родительский класс Здания
import material


class Buildings:
    def __init__(self, material: str, floors: int, flats: int):
        self.__material = material  # материалы для постройки здания
        self.floors = floors  # количество этажей здания
        self.flats = flats  # количество квартир здания

    # метод, возвращающий информацию о здании с использованием атрибутов класса
    # в виде строки с неформальным представлением объекта
    def __str__(self):
        return (f"Спроектированное здание из {self.__material} "
                f"имеет {self.floors} этажей и {self.flats} квартир")

    # метод, возвращающий информацию о здании с использованием атрибутов класса
    # в виде строки с формальным представлением объекта
    def __repr__(self):
        return f"Buildings({self.__material}, {self.floors}, {self.flats})"

    # метод Getter - возвращает значение в атрибут класса
    @property
    def private_material(self):
        return self.private_material

    # метод Setter - получает значение из атрибута класса
    @material.setter
    def private_material(self, value: str):
        if value == "concrete" or value == "wood":
            self.__material = value

    # метод подсчета количества квартир на этаже
    def count_flats_on_the_floor(self):
        return self.floors / self.flats

    # метод увеличения этажей
    def add_floor(self):
        self.floors += 1
