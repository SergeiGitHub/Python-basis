list=[7, 5, 3, 3, 2]
print(list)
m=len(list)
n=int(input("Введите положительное число, новый элемент рейтинга: "))

for el in list:
    if n > el:
        list.insert(list.index(el), n)
        break
    elif list[m-1] >= n:
        list.append(n)
        break
print(list)