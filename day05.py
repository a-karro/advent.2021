from collections import Counter

lines = []
for i in open("data/day05.txt", "r").read().splitlines():
    lines.append(list(map(int, i.replace(" -> ", ",").split(","))))

field_p1 = []
field_p2 = []


def order(a, b):
    return (a, b) if a < b else (b, a)


def cmp(a, b):
    return (a > b) - (a < b)


for line in lines:
    if line[0] == line[2] or line[1] == line[3]:
        if line[0] == line[2]:
            s, f = order(line[1], line[3])
            for y in range(s, f + 1):
                field_p1.append((line[0], y))
        else:
            s, f = order(line[0], line[2])
            for x in range(s, f + 1):
                field_p1.append((x, line[1]))
    else:
        if line[1] > line[3]:
            line = line[2:] + line[:2]
        ofs = cmp(line[0], line[2])
        x = line[0]
        for y in range(line[1], line[3] + 1):
            field_p2.append((x, y))
            x -= ofs

print("Puzzle 5.1", sum(1 for i in Counter(field_p1).values() if i > 1))
print("Puzzle 5.2", sum(1 for i in Counter(field_p1 + field_p2).values() if i > 1))
