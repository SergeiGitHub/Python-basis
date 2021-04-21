from random import randint

list_turn = ["направо", "налево", "прямо", "в обратном направлении"]


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.my_list = [speed, color, name, is_police]

    def go(self):
        print(f"{self.my_list[2]} поехала")
        if self.my_list[3] == "police":
            self.my_list[3] = True
            print(f"Машина полицейская: {self.my_list[3]}")
        else:
            self.my_list[3] = False
            print(f"Машина полицейская: {self.my_list[3]}")

    def stop(self):
        print(f"{self.my_list[2]} остановилась")

    def turn(self):
        print(f"Машина поехала: {list_turn[randint(0, 3)]}")

    def show_speed(self):
        print(f"Текущая скорость авто: {self.my_list[0]}")


class TownCar(Car):
    def show_speed(self):  # свыше 60 - превышение
        if self.my_list[0] > 60:
            print("Превышение скорости, более 60")
        else:
            super().show_speed()


class SportCar(Car):
    def sport_method(self):
        print("Это метод из дочернего класса SportCar")


class WorkCar(Car):
    def show_speed(self):
        if self.my_list[0] > 40:
            print("Превышение скорости, более 40")
        else:
            super().show_speed()


class PoliceCar(Car):
    def police_method(self):
        print("Это метод из дочернего класса PoliceCar")


a = TownCar(50, "green", "BMW", "police")
a.go()
a.stop()
a.turn()
a.show_speed()
print()

b = SportCar(30, "white", "Lada", "not police")
b.sport_method()
b.stop()
print()

c = WorkCar(55, "red", "Audi", "not police")
c.go()
c.stop()
c.turn()
c.show_speed()
print()

d = PoliceCar(70, "black", "Mers", "police")
d.police_method()
d.go()