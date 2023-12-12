from collections import OrderedDict

n = int(input())

dictionary = OrderedDict()

for _ in range(n):
    item = input().rsplit(' ', 1)
    if item[0] in dictionary:
        dictionary[item[0]] = dictionary[item[0]] + int(item[1])
    else:
        dictionary[item[0]] = int(item[1])

for key, value in dictionary.items():
    print(key, value)