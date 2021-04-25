from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def my_method(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def my_method(self):
        exp_coat = round(self.size / 6.5) + 0.5
        print(f"Расход ткани для пальто: {exp_coat}")
        return exp_coat


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def my_method(self):
        exp_costume = 2 * self.height + 0.3
        print(f"Расход ткани для костюма: {exp_costume}")
        return exp_costume


a = Coat(7)
b = Costume(7)
print(f"Общий расход ткани: {a.my_method + b.my_method}")
