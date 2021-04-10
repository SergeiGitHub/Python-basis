def my_f6():
    #global list
    #list = input("Введите слова из маленьких латинских букв: ").lower().title().split()

    n = 0 # счетчик индекса списка list
    while n <= len(list)-1:
        for i in list[n]:
            if i.lower() in kiril:
                list.pop(n)
                n -= 1
                break
        n += 1
    return list


kiril = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
         "х", "ц", "ч", "ш", "ъ", "ы", "ь", "э", "ю", "я")

list = input("Введите слова из маленьких латинских букв: ").lower().title().split()
print(my_f6())

list2=input("Введите дополнительные слова из латинских букв в нижнем регистре для добавления: ").lower().title().split()
list=list+list2
print(my_f6())