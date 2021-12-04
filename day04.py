data = []
with open("data/day04.txt", "r") as f:
    inp = list(map(int, f.readline().split(",")))
    for k in f.read().splitlines():
        if k != '':
            data.extend([(int(c), 0) for c in k.split()])

p1 = False
boards_seen = [0] * (len(data) // 25)

lb = -1
lbv = 0

for d in inp:
    for cnt, x in enumerate(data):
        if x[0] == d:
            data[cnt] = (x[0], 1)

    board = -1
    lb = -1
    for i in range(len(data) // 5):
        if sum(x[1] for x in data[i * 5: (i + 1) * 5]) == 5:
            board = i // 5
            if boards_seen[board] == 0:
                lb = board
                boards_seen[lb] = 1

    for i in range(len(data) // 25):
        for cl in range(5):
            if sum(x[1] for x in data[i * 25 + cl: (i + 1) * 25 + cl: 5]) == 5:
                board = i
                if boards_seen[board] == 0:
                    lb = board
                    boards_seen[lb] = 1

    if lb != -1:
        lbv = sum(x[0] for x in data[lb * 25:(lb + 1) * 25] if x[1] == 0) * d
        if not p1:
            print("Puzzle 4.1:", lbv)
            p1 = True

print("Puzzle 4.2:", lbv)
