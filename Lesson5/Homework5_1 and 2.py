with open("1.txt", "w+", encoding="utf-8") as file:
    while True:
        text = input("Введите данные для записи, для окончания записи введите пустую строку: ")
        if text == "":
            break
        file.writelines(f"{text}\n")

    file.seek(0)
    # print(file.readlines())

    i = 1
    for line in file:
        nw = 0
        for el in line.split():
            nw += 1
        print(f"Строка {i}, в ней следующая запись: {line}. Кол-во слов: {nw}")
        i += 1

    print(f"Общее кол-во непустых строк: {i-1}")