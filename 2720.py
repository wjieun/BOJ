money = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    C = int(input())
    for m in money:
        if C >= m: print(C // m, end=' '); C %= m
        else: print(0, end=' ')
    print()