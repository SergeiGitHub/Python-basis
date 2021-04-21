class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def mass(self, thickness=int(input("Введите толщину полотна в см: ")), weight=25):
        self.weight = weight
        m = self._length * self._width * self.weight * thickness
        print(f"Масса асфальта = {round(m / 1000)} т.")


a = Road(5000, 20)
a.mass()
print(f"Длина асфальта: {a._length} м")
print(f"Ширина асфальта: {a._width} м")
print(f"Масса асфальта для покрытия 1 кв.м толщиной 1 см: {a.weight} кг")
