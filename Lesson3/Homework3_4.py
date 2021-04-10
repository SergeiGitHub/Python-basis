def my_func(x, y):
    return x**y


x = float(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))

while True:
    if x <= 0:
        x = float(input("Введите действительное положительное число: "))
    elif y >= 0:
        y = int(input("Введите целое отрицательное число: "))
    else:
        print(my_func(x, y))
        break
