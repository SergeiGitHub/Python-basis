from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

k = 0
for i in cycle([1, True, "srr", {3, 6}, [9, 7]]):
    if k > 10:
        break
    print(i)
    k += 1
