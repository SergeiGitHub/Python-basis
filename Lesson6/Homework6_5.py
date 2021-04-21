class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}. Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title}. Запуск дочернего метода Pen")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}. Запуск дочернего метода Pencil")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title}. Запуск дочернего метода Handle")

a = Stationery("Канцелярия")
a.draw()

b = Pen("Ручка")
b.draw()

c = Pencil("Карандаш")
c.draw()

d = Handle("Маркер")
d.draw()