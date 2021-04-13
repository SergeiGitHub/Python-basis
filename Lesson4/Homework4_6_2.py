from sys import argv
from itertools import cycle

script_name, qt = argv

k = 0
elements=[678, True, "str", {3, 6}, [9, 7]]
for i in cycle(elements):
    if k == int(qt):
        break
    print(i)
    k += 1


# print("Имя скрипта: ", script_name)
print("Введенное кол-во повторений элементов списка: ", qt)

