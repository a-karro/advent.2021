def all_(this, where):
    return all(c in where for c in this)


def get_digits(inp):
    res = [""] * 10
    res[1] = next(i for i in inp if len(i) == 2)
    res[7] = next(i for i in inp if len(i) == 3)
    res[4] = next(i for i in inp if len(i) == 4)
    res[8] = next(i for i in inp if len(i) == 7)
    res[3] = next(i for i in inp if len(i) == 5 and all_(res[7], i))
    res[0] = next(
        i for i in inp if len(i) == 6 and all_(res[7], i) and not all_(res[3], i))
    res[9] = next(i for i in inp if len(i) == 6 and all_(res[3], i) and all_(res[4], i))
    res[5] = next(i for i in inp if len(i) == 5 and all_(i, res[9]) and i != res[3])
    res[2] = next(i for i in inp if len(i) == 5 and i != res[5] and i != res[3])
    res[6] = next(i for i in inp if len(i) == 6 and i != res[0] and i != res[9])
    return res


data = open("data/day08.txt", "r").read().splitlines()


ins = []
outs = []
for d in data:
    k = d.split(" | ")
    ins.append(["".join(sorted(m)) for m in k[0].split()])
    outs.append(["".join(sorted(m)) for m in k[1].split()])

ao = [i for e in outs for i in e]
print("Puzzle 8.1:", sum(1 for i in ao if len(i) in [2, 3, 4, 7]))


s = 0
for i, k in enumerate(ins):
    digs = get_digits(k)
    s += int("".join(str(digs.index(a)) for a in outs[i]))

print("Puzzle 8.2:", s)
