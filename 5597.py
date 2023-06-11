std = [x for x in range(1, 31)]

for _ in range(28):
    std.remove(int(input()))

for s in std:
    print(s)