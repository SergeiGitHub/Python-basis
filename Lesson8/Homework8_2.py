class MyZeroDivErr(Exception):
    def __init__(self, text):
        self.text = text

a = input("Введите числитель: ")
b = input("Введите знаменатель: ")

try:
    a, b = int(a), int(b)
    # фильтр
    if b == 0:
        raise MyZeroDivErr("Error! My Zero Division")
except (ValueError, MyZeroDivErr) as err:
    print(err)
else:
    print(a / b)
