# импорт аргументов командной строки
from sys import argv

script_name, hrs, rate, bonus = argv # распаковка содержимого списка argv в переменные
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hrs)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Заработная плата сотрудника, (выработка в часах * ставка в час) + премия :", (int(hrs)*int(rate))+int(bonus))

