N, M = input().split()
N = int(N); M = int(M)

cnt = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = input().split()
    i = int(i); j = int(j)
    tmp = cnt[i - 1]
    cnt[i - 1] = cnt[j - 1]
    cnt[j - 1] = tmp

for c in cnt:
    print(c, end=' ')
