from sys import argv
from itertools import count

script_name, number = argv # распаковка содержимого списка argv в переменные

num=int(number)
for el in count(num):
    if el > 10:
        break
    else:
        print(el)

print("Имя скрипта: ", script_name)
print("Введенное число до 10: ", number)

