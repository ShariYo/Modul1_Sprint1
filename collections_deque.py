from collections import deque

N = int(input())

d = deque()

for _ in range(N):
    fu = input().lower()
    if fu.split()[0] == 'append':
        d.append(fu.split()[1])
    elif fu.split()[0] == 'appendleft':
        d.appendleft(fu.split()[1])
    elif fu.split()[0] == 'pop':
        d.pop()
    elif fu.split()[0] == 'popleft':
        d.popleft()

print(*d)
