wage = 25000
bonus = 5000
my_dict = {'wage': wage, 'bonus': bonus}


class Worker:
    def __init__(self, n, s, p, i=my_dict):
        self.my_list=[n, s, p, i]
        #self.name = n
        #self.surname = s
        #self.position = p
        #self._income = i

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника - {self.my_list[0]} {self.my_list[1]}")

    def get_total_income(self):
        print(f"Доход с учетом премии - {sum(self.my_list[3].values())}")

a = Position("Sergei", "Pavlov", "engineer")
a.get_full_name()
a.get_total_income()