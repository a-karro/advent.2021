with open("data/day02.txt", "r") as f:
    data = f.read().splitlines()

fwd = d1 = d2 = 0

for i in data:
    if "forward" in i:
        x = int(i.replace("forward ", ""))
        fwd += x
        d2 += x * d1
    else:
        d1 += int(i.replace("up ", "-").replace("down ", ""))

print("Puzzle 2.1:", fwd * d1)
print("Puzzle 2.2:", fwd * d2)
