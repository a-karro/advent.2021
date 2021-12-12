import math

data = open("data/day11.txt", "r").read().splitlines()

octo = [[-math.inf] * (len(data[0]) + 2) for _ in range(len(data) + 2)]
for i, d in enumerate(data):
    for k, c in enumerate(d):
        octo[i + 1][k + 1] = int(c)

RX = range(1, len(octo) - 1)
RY = range(1, len(octo[0]) - 1)
N = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def add_p(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


fc = 0
t = 0
while True:
    t += 1
    octo = [[a + 1 for a in b] for b in octo]
    fl = [(y, x) for y in RY for x in RX if octo[y][x] > 9]
    done = fl.copy()
    while fl:
        c = fl.pop()
        for k in [add_p(c, n) for n in N]:
            if k in done:
                continue
            octo[k[0]][k[1]] += 1
            if octo[k[0]][k[1]] > 9:
                fl.append(k)
                done.append(k)
    for c in done:
        octo[c[0]][c[1]] = 0
    fc += len(done)
    if t == 100:
        print("Puzzle 11.1:", fc)

    if sum(octo[y][x] for y in RY for x in RX) == 0:
        print("Puzzle 11.2:", t)
        break
