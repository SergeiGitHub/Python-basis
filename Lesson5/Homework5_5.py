# Вариант 1 задания 5
from random import randint

list = [randint(0, 9) for _ in range(1, randint(2, 12))]
print(*list)

sum = 0
for el in list:
    with open("5.txt", "a", encoding="utf-8") as numbers:
        numbers.writelines(f"{el} ")
        sum += el

print(f"Сумма чисел в файле: {sum}")
