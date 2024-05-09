from math import sqrt

min_num, max_num = input().split()
min_num = int(min_num)
max_num = int(max_num)
MAX = 1000000

prime_bool = [True for _ in range(0, MAX + 1)]
for i in range(2, int(sqrt(MAX)) + 1):
    if prime_bool[i]:
        for j in range(2, int(MAX / i) + 1):
            if i * j <= MAX: prime_bool[i * j] = False

square = []
for i in range(2, MAX + 1):
    if prime_bool[i]: square.append(i * i)

cnt = max_num - min_num + 1
num_bool = [True for _ in range(0, cnt)]
for s in square:
    if min_num % s == 0: min_idx = int(min_num / s)
    else: min_idx = int(min_num / s) + 1
    max_idx = int(max_num / s)
    for i in range(min_idx, max_idx + 1):
        num_bool[s * i - min_num] = False

print(num_bool.count(True))