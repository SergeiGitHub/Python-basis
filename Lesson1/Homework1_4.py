max = 0
num = int(input("Введите целое число: "))

while num > 0:
    if num % 10 > max:
        max = num % 10
    num = num // 10

print(max)
