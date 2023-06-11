N, B = input().split()
N = int(N); B = int(B)
result = ""

while N >= B:
    quotient = N % B
    if quotient >= 10: quotient = chr(quotient + 55)
    result += str(quotient)
    N //= B

if N >= 10: N = chr(N + 55)
result += str(N)

print(result[::-1])