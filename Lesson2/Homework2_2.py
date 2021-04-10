elements = input("Введите элементы списка разделяя пробелом: ")
elements_list = elements.split()
# print(elements_list)

# copy_elements_list = elements_list.copy()

for el in elements_list:
    if elements_list.index(el)!=0 and elements_list.index(el) % 2 != 0:
        elements_list.insert(elements_list.index(el)-1, el)
        elements_list.pop(elements_list.index(el)+2)

print(elements_list)
