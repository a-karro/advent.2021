import math
data = open("data/day09.txt", "r").read().splitlines()


def get_basin(x, y, seen):
    seen.append((x, y))
    for nxt in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
        if nxt not in seen and points[nxt[1]][nxt[0]] < 9:
            get_basin(*nxt, seen)


points = [[9] * (len(data[0]) + 2) for _ in range(len(data) + 2)]
for i, d in enumerate(data):
    for k, c in enumerate(d):
        points[i+1][k+1] = int(c)

lps = []
for y in range(1, len(data)+1):
    for x in range(1, len(data[0])+1):
        if min(points[y-1][x], points[y+1][x], points[y][x-1], points[y][x+1]) > points[y][x]:
            lps.append((x, y, points[y][x] + 1))
print("Puzzle 9.1:", sum(c[2] for c in lps))


b = []
for lp in lps:
    seen = []
    get_basin(lp[0], lp[1], seen)
    b.append(len(seen))
b = sorted(b)
print("Puzzle 9.2:", math.prod(b[-3:]))
