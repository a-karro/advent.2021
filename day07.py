from functools import lru_cache
from math import inf

data = list(map(int, open("data/day07.txt", "r").read().split(",")))


@lru_cache(None)
def sum_all(n):
    return sum(c for c in range(abs(n) + 1))


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
        x += sum_all(abs(a-b))
    if m >= x:
        m = x
print("Puzzle 7.2:", m)
