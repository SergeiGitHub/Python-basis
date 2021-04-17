import json

my_dict = dict()

with open("text_7.txt", "r", encoding="utf-8") as companies:
    # print(companies.read())
    total = 0
    i = 0
    for line in companies:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        my_dict.update({line[0]: profit})
        # print(profit)
        if profit > 0:
            total += profit
            i += 1

avg = total / i
print(f"Средняя прибыль безубыточных фирм: {avg}")
print(my_dict)
my_dict2 = {'average profit': total / i}
my_list = [my_dict, my_dict2]
print(my_list)

with open("text_777.json", "w", encoding="utf-8") as file:
    json.dump(my_list, file, indent=4, ensure_ascii=False)
