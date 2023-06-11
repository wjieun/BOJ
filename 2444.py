N = int(input())
for i in range(1, 2 * N):
    if i > N:
        i = (2 * N) - i
    a = i * 2 - 1
    b = int((N * 2 - a) / 2)
    print(" " * b + "*" * a)