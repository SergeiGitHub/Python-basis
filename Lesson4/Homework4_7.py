from math import factorial

# def gen():
#    for el in (1,2,3):
#        yield factorial(el)

n = int(input("Введите число n для расчета факториалов с 1 до n: "))
fact = (num for num in range(1, n + 1))


def gen():
    for el in fact:
        yield factorial(el)


print(gen())
i=1
for k in gen():
    print(f"Факториал числа {i} равен: {k}")
    i+=1
