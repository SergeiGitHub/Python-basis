my_dict = dict()
with open("text_6.txt", "r", encoding="utf-8") as subjects:
    # print(subjects.read())
    for line in subjects:
        line = line.split(": ")
        # print(line[1], end="")
        str = ""
        q = 0
        for el in line[1]:
            if el.isnumeric():
                str += el
            elif str != "" and not el.isnumeric():
                q += int(str)
                str=""

        my_dict.update({line[0]: q})

print(my_dict)
