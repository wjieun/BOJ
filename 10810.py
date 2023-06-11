N, M = input().split()
N = int(N); M = int(M)

cnt = [0 for _ in range(N)]

for _ in range(M):
    L = list(map(int, input().split()))
    i = L[0]; j = L[1]; k = L[2]
    for n in range(i - 1, j):
        cnt[n] = k

for c in cnt:
    print(c, end=' ')