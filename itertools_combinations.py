from itertools import combinations

word = input().rsplit(' ', 1)

line_list = []
for nr in range(int(word[1]) + 1):
    if nr == 0:
        pass
    else:
        for line in list(combinations(word[0], nr)):
            line_list.append(tuple(sorted(line)))

line_list_sorted = sorted(line_list, key=lambda x: (len(x), x))
for one in line_list_sorted:
    print(''.join(one))