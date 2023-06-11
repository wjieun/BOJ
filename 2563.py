N = int(input())
paper = [[False for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = input().split()
    x = int(x); y = int(y)
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = True

cnt = [paper[i].count(True) for i in range(100)]
print(sum(cnt))