# Дочерний класс Коттеджи

from Buildings import Buildings


class Cottage (Buildings):
    def __init__(self, material: str, floors: int, flats: int, location: float, square: float):
        super.__init__(material, floors, flats)  #унаследование конструктора от базового/родительского класса
        self.location = location  # местоположение коттеджа
        self.square = square  # площадь коттеджа

# метод, возвращающий информацию о здании с использованием атрибутов класса
# в виде строки с неформальным представлением объекта
def __str__(self):
    return (f"Спроектированное здание из {self.__material}"
            f"имеет {self.floors} этажей и {self.flats} квартир"
            f"имеет площадь = {self.square} и расположение в координатах {self.location}")

# метод, возвращающий информацию о здании с использованием атрибутов класса
# в виде строки с формальным представлением объекта
def __repr__(self):
    return f"Buildings({self.__material}, {self.floors}, {self.flats}, {self.location}, {self.square})"