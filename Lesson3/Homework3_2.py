def my_f(name, surname, bithyear, city, email, mobile):
    return [name, surname, bithyear, city, email, mobile]


print(*my_f(name=input("Введите имя: "), surname=input("Введите фамилию: "), bithyear=input("Введите год рождения: "),
           city=input("Введите город проживания: "), email=input("Введите электронную почту: "),
           mobile=input("Введите номер тедефона: ")))
