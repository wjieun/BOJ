N = int(input())
num = list(map(int, input().split()))

primes = []
for n in num:
    is_prime = True
    if n == 1: is_prime = False
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime: primes.append(n)
print(len(primes))