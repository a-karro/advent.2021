from collections import Counter


MOST = "1"
LEAST = "0"


def filter_list(this, sign):
    t = this
    while len(t) > 1:
        for p in range(len(t[0])):
            counts = Counter([t[i][p] for i in range(len(t))])
            mc = counts.most_common()[0]
            lc = counts.most_common()[-1]
            check = mc[0] if sign == MOST else lc[0]
            if mc[1] == lc[1]:
                check = sign
            t = [o for o in t if o[p] == check]
            if len(t) == 1:
                break
    return t[0]


data = open("data/day03.txt", "r").read().splitlines()

mc = lc = ""
ll = len(data[0])
dl = len(data)
for p in range(ll):
    counts = Counter(data[i][p] for i in range(dl))
    mc += counts.most_common()[0][0]
    lc += counts.most_common()[-1][0]

print("Puzzle 3.1:", int(mc, 2) * int(lc, 2))
print("Puzzle 3.2:",
      int(filter_list(data, MOST), 2) * int(filter_list(data, LEAST), 2))
