# Вариант 2 задания 5
from random import randint

list = [randint(0, 9) for _ in range(1, randint(2, 12))]
print(*list)

sum = 0

with open("5.txt", "a+", encoding="utf-8") as numbers:
    for el in list:
        numbers.writelines(f"{el} ")

    numbers.seek(0)
    print(numbers.read())
    numbers.seek(0)

    for line in numbers:
        for el in line.split():
            sum += int(el)

print(f"Сумма чисел в файле: {sum}")
