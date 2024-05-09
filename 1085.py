num = list(map(int, input().split()))
x = num[0]; y = num[1]; w = num[2]; h = num[3]
dist = [x, y, w - x, h - y]
print(min(dist))