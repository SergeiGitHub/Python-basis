rev = int(input("Укажите выручку: "))
exp = int(input("Введите издержки: "))

if rev > exp:
    print(f"Выручка больше издержек, прибыль: {rev - exp}")
    print(f"Рентабельность выручки составляет: {((rev - exp) / rev) * 100:.2f}%")
    q=int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {(rev-exp)/q}")
elif rev == exp:
    print("Выручка равна издержкам")
else:
    print(f"Издержки больше выручки, убыток: {exp - rev}")
