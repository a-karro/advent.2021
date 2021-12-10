from functools import reduce
data = open("data/day10.txt", "r").read().splitlines()

val = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

pairs = ["()", "[]", "<>", "{}"]
s = 0
inc = []
for d in data:
    while any(i in d for i in pairs):
        for p in pairs:
            d = d.replace(p, "")
    try:
        s += next(val[i] for i in d if i in ">}])")
    except StopIteration:
        inc.append(reduce(lambda a, b: a * 5 + b, [val[v] for v in d[::-1]]))

inc = sorted(inc)

print("Puzzle 10.1:", s)
print("Puzzle 10.2:", inc[len(inc) // 2])
