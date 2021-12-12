from collections import defaultdict

d = defaultdict(list)
for a in open("data/day12.txt", "r").read().splitlines():
    k, v = a.split("-")
    d[k].append(v)
    d[v].append(k)


def find_all_paths(graph, start, end, path=None, ignore=None):
    path = (path or []) + [start]
    ignore = ignore or []
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if 65 <= ord(node[0]) <= 97 or node not in path or node in ignore:
            x = ignore.copy()
            if node in x:
                x = x[:-1]
            new = find_all_paths(graph, node, end, path, x)
            for np in new:
                paths.append(np)
    return paths


print("Puzzle 12.1:", len(find_all_paths(d, "start", "end")))


p = []
for n in d.keys():
    if n in ["start", "end"] or 65 <= ord(n[0]) <= 97:
        continue
    p.extend(find_all_paths(d, "start", "end", None, [n, n]))

print("Puzzle 12.2:", len(set(tuple(c) for c in p)))
