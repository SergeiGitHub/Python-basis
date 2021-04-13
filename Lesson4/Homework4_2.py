#my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list=input("Введите числа для списка через пробел: ").split()

new_list = [int(num) for num in my_list if int(num) > int(my_list[my_list.index(num) - 1]) and my_list.index(num) - 1 >= 0]
print(new_list)
