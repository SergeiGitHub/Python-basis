with open("text_3.txt", "r", encoding="utf-8") as salaries:
    compare = 20000
    sum = 0
    q = 0
    list = []
    for line in salaries:
        line = line.split()
        sum = sum + float(line[1])
        q += 1
        if float(line[1]) < compare:
            print(f"Получает менее 20 тыс: {line[0]}")
            list.append(line[0])  # 2-й варант создания и вывода списка сотрудников с ЗП менее 20 тыс
    print(f"Список всех, кто получает менее 20 тыс: {list}") # 2-й варант
    print(f"Средняя величина дохода: {sum / q}")