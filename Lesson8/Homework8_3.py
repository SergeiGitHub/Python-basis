class CheckIfNumbers(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
try:
    while True:
        num = input("Введите число, для завершения введите stop: ")
        if num.isdigit():
            my_list.append(num)
        elif num == "stop":
            break
        elif not num.isdigit():
            # continue
            print(CheckIfNumbers("Ошибка! Необходимо вводить только цифры"))
except CheckIfNumbers as err:
    print(err)
else:
    print(my_list)
finally:
    print(my_list)
