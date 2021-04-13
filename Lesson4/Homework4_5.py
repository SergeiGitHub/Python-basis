from functools import reduce

new_list = [num for num in list(range(100, 1001)) if num % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, new_list))
