C = int(input())
for i in range(0, C):
    N = list(map(int, input().split()))
    avg = (sum(N, 0.0) / N[0]) - 1
    count = 0
    for j in range(1, len(N)):
        if N[j] > avg: count += 1
    print('{:.3f}%'.format(count/N[0]*100))