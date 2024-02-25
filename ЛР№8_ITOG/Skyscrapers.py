# дочерний класс Небоскрёбы

from Buildings import Buildings


class Skyscraperers (Buildings):
    def add_floor(self, incriment:int):
        self.floors += incriment