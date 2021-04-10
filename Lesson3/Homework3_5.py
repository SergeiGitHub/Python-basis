def func():
    global sum
    sum = 0
    for el in list:
        if el.upper() == "Q":
            break
        else:
            sum = sum + int(el)
    return sum


sum2 = 0
while True:
    list = input("Введите числа разделяя их пробелом. "
                 "Выполнение программы завершится при вводе символа q: ").split()
    print(list)
    func()
    sum2 = sum + sum2
    print("Сумма: " + str(sum) + " Общая сумма: " + str(sum2))
    if "q" in list or "Q" in list:
        break