list = ["зима", "весна", "лето", "осень"]
m = int(input("Введите порядковый номер месца от 1 до 12: "))

while True:
    if m < 1 or m > 12:
        m = int(input("Введите порядковый номер месца от 1 до 12: "))
    else:
        if m == 1 or m == 2 or m == 3:
            print(list[0])
        elif m == 4 or m == 5 or m == 6:
            print(list[1])
        elif m == 7 or m == 8 or m == 9:
            print(list[2])
        elif m == 10 or m == 11 or m == 12:
            print(list[3])
        break
