from math import inf

data = list(map(int, open("data/day07.txt", "r").read().split(",")))


m = inf
for a in range(max(data)):
    x = sum(abs(a-b) for b in data)
    if x < m:
        m = x
print("Puzzle 7.1:", m)


m = inf
for a in range(max(data)):
    x = 0
    for b in data:
        n = abs(a-b)
        x += n * (n + 1) // 2
    if m >= x:
        m = x
print("Puzzle 7.2:", m)
