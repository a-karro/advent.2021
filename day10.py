from functools import reduce
data = open("data/day10.txt", "r").read().splitlines()

val = dict(zip("([{<>}])", [1, 2, 3, 4, 25137, 1197, 57, 3]))

pairs = ["()", "[]", "<>", "{}"]
s = 0
inc = []
for d in data:
    while any(i in d for i in pairs):
        d = reduce(lambda a, b: a.replace(b, ""), pairs, d)
    try:
        s += next(val[i] for i in d if i in ">}])")
    except StopIteration:
        inc.append(reduce(lambda a, b: a * 5 + b, map(val.get, d[::-1])))

inc = sorted(inc)

print("Puzzle 10.1:", s)
print("Puzzle 10.2:", inc[len(inc) // 2])
