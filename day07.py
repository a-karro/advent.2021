d = list(map(int, open("data/day07.txt", "r").read().split(",")))
r = range(min(d), max(d) + 1)
print("Puzzle 7.1:", min(sum(abs(a - b) for b in d) for a in r))
print("Puzzle 7.2:", min(sum(abs(a - b) * (abs(a - b) + 1) // 2 for b in d) for a in r))
