sec_org = int(input("Введите время в секундах: "))
print(sec_org)
hr = sec_org // 3600
min = (sec_org % 3600) // 60
sec = (sec_org % 3600) % 60
print(f"Время в формате чч:мм:сс {hr:0>2d}:{min:0>2d}:{sec:0>2d}")
