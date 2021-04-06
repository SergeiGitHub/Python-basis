dict={"зима": [1, 2, 3], "весна": [4, 5, 6], "лето": [7, 8, 9], "осень": [10, 11, 12]}
print(type(dict))

m = int(input("Введите порядковый номер месца от 1 до 12: "))

for k, v in dict.items():
    if m in v:
        print(k)
        break