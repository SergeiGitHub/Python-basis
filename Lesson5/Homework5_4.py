my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text_4.txt", "r", encoding="utf-8") as engnumbers:
    # print(engnumbers.read())
    for line in engnumbers:
        line = line.split()
        if line[0] in my_dict.keys():
            # print(my_dict.get(line[0]))
            with open("text_44.txt", "a", encoding="utf-8") as rusnumbers:
                # rusnumbers.write()
                rusnumbers.write(f"{my_dict.get(line[0])} {line[1]} {line[2]}\n")
                # print(my_dict.get(line[0]), file=rusnumbers)


