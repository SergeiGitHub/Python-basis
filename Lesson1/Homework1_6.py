a = float(input("Введите кол-во км в первый день, a: "))
b = float(input("Введите необходимое кол-во км, b: "))

i = 1
while a < b:
    a = a * 1.1
    i += 1

print(f"на {i} день спортсмен достиг {a:.2f} км — не менее {b} км.")
