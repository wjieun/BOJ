N, B = input().split()
B = int(B)
result = 0

for i in range(len(N)):
    if ord(N[i]) > 64: num = ord(N[i]) - 55
    else: num = int(N[i])
    i = len(N) - 1 - i
    result += num * (B ** i)

print(result)