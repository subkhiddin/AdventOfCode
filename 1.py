from collections import Counter

# Read input from file
with open("input.txt") as f:
    ls = f.read().strip().split("\n")

# Process input to separate pairs into two lists
l1, l2 = zip(*[map(int, x.split()) for x in ls])

# Part 1: Calculate the sum of absolute differences between sorted pairs
print("Part 1:", sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2))))

# Part 2: Use Counter to compute the weighted sum
cs = Counter(l2)
print("Part 2:", sum(x * cs[x] for x in l1))
