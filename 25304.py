X = int(input())
N = int(input())

result = 0
for _ in range(0, N):
    a, b = input().split()
    result += int(a) * int(b)

if X == result: print("Yes")
else: print("No")