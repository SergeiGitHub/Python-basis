def my_f(a, b, c):
    summax2 = a + b + c - min(a, b, c)
    return summax2


print(my_f(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
           int(input("Введите третье число: "))))
