N, K = input().split()
N = int(N); K = int(K)

cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
if cnt < K: print(0)