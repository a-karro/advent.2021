dots, folds = open("data/day13.txt", "r").read().split("\n\n")
dots = [int(k) for d in dots.split("\n") for k in d.split(",")]
field = [[0] * (max(dots[::2]) + 1) for _ in range(max(dots[1::2]) + 1)]

for i in range(0, len(dots), 2):
    field[dots[i+1]][dots[i]] = 1


def fold(this, by):
    v = int(by.split("=")[1])
    if "x" in by:
        ff = [a[v+1:][::-1] for a in this]
        rr = [a[:v] for a in this]
        r = [[sum(pair) for pair in zip(*pairs)] for pairs in zip(rr, ff)]
    else:
        ff = this[v+1:][::-1]
        rr = this[:v]
        r = [[sum(pair) for pair in zip(*pairs)] for pairs in zip(rr, ff)]
    return r


p1 = True
for f in folds.split("\n"):
    field = fold(field, f.replace("fold along ", ""))
    if p1:
        print("Puzzle 13.1:",
              sum(1 if x > 0 else 0 for x in [a for b in field for a in b]))
        p1 = False

print("Puzzle 13.2:")
for c in field:
    print("".join(["  " if z == 0 else "##" for z in c]))
