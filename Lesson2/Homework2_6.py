
list = list()
n = int(input("Сколько хотите добавить товаров: "))

i = 0
while i < n:
    name = input("Введите название товара " + str(i+1) + " : ")
    price = input("Введите цену товара: ")
    q = input("Введите кол-во товара: ")
    unit = input("Введите единицу измерения товара: ")
    dict = {"название": name, "цена": price, "количество": q, "ед": unit}
    tuple = (i + 1, dict)
    list.insert(i, tuple)
    print(list)
    i += 1

# dict2={"название": [list[0][1].values()], "цена": [], "количество": [], "ед": []}
# dict2 = {"название": [list[0][1].get("название")], "цена": [list[0][1].get("цена")],
#       "количество": [list[0][1].get("количество")], "ед": [list[0][1].get("ед")]}

list_name=[]
list_price=[]
list_q=[]
list_unit=[]
i=0
for el in list:
    list_name.insert(list.index(el)-1, list[i][1].get("название"))
    list_price.insert(list.index(el) - 1, list[i][1].get("цена"))
    list_q.insert(list.index(el) - 1, list[i][1].get("количество"))
    list_unit.insert(list.index(el) - 1, list[i][1].get("ед"))
    i+=1

dict2={"название": list_name, "цена": list_price, "количество": list_q, "ед": list_unit}
print(dict2)