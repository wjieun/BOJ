L = int(input())
s = sorted(list(map(int, input().split())))
n = int(input())

min_num = 0
max_num = 0

for i in s:
    if i < n:
        min_num = i + 1
    elif i == n:
        min_num = 0
        max_num = 0
        break
    elif i > n:
        max_num = i - 1
        break

if max_num == 0:
    print(0)
else:
    if min_num == 0:
        min_num = 1
    min_cnt = n - min_num + 1
    max_cnt = max_num - n + 1
    print(min_cnt * max_cnt - 1)