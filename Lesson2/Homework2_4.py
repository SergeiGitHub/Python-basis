words = input("Введите слова разделяя их пробелом: ")
list=words.split()
# print(list)

for ind, el in enumerate(list, 1):
    print(ind, el[0:10])