from collections import Counter

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

l1, l2 = zip(*[map(int, x.split()) for x in ls])


print("Part 1:", sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2))))

cs = Counter(l2)
print("Part 2:", sum(x * cs[x] for x in l1))
