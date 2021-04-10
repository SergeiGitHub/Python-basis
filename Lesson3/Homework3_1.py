def my_f(a, b):
    c = a / b
    return c


a = float(input("Введите числитель: "))
b = float(input("Введите знаменатель: "))

try:
    print(my_f(a,b))
except ZeroDivisionError:
    print("Ошибка! Деление на ноль запрещено!")
