N = int(input())
score = list(map(int, input().split()))
m = max(score)
for i in range(0, N):
    score[i] *= 100/m
avg = sum(score, 0.0) / N
print(avg)