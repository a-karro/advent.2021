data = [int(i) for i in open("data/day01.txt", "r").read().splitlines()]

print("Puzzle 1.1:", sum(1 for a in range(1, len(data)) if data[a] > data[a - 1]))

win = [sum(data[k] for k in range(a, a + 3)) for a in range(len(data) - 2)]
print("Puzzle 1.2:", sum(1 for a in range(1, len(win)) if win[a] > win[a - 1]))
