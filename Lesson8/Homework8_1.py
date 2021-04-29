class DMY:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def validation(obj):
        if obj.d >= 1 and obj.d <= 30:
            print(f"Номер дня: {obj.d}")
        else:
            print("День должен быть в диапазоне от 1 до 30")

        if obj.m >= 1 and obj.m <= 12:
            print(f"Номер месяца: {obj.m}")
        else:
            print("Номер месяца должен быть в диапазоне от 1 до 12")

        print(f"Год: {obj.y}") if obj.y >= 1 and obj.y <= 9999 else \
            print("Год должен быть в диапазоне от 1 до 9999")

    @classmethod
    def to_number(cls, data):  # получаем данные data через return(cls)
        try:
            d, m, y = data.split("-")  # распаковываемся в день, месяц, год. split - строку в список
            cls.d = int(d)
            cls.m = int(m)
            cls.y = int(y)
            return cls(data)
            # return cls(d, m, y)
        except (ValueError, NameError) as err:
            print("Некорретно введены данные. Ошибка!")


# a = "23-04-2021"
a = input("Введите дату в формате dd-mm-yyyy:")
# one = DMY("23-04-2021")
one = DMY.to_number(a)
DMY.validation(one)
