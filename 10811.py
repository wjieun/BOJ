N, M = input().split()
N = int(N); M = int(M)

cnt = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = input().split()
    i = int(i); j = int(j);

    if i != j:
        sum = i + j
        for k in range(i, int(sum / 2) + 1):
            tmp = cnt[k - 1]
            cnt[k - 1] = cnt[sum - k - 1]
            cnt[sum - k - 1] = tmp

for c in cnt:
    print(c, end=' ')