data = list(map(int, open("data/day06.txt", "r").read().split(",")))

limit = 256
days = [0] * (limit + 9)
for i in data:
    days[i] += 1

for i in range(limit):
    days[i + 9] += days[i]
    days[i + 7] += days[i]

print("Puzzle 6.1:", sum(days[:80]) + len(data))
print("Puzzle 6.2:", sum(days[:limit]) + len(data))
