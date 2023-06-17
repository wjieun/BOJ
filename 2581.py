M = int(input())
N = int(input())

num = [i for i in range(M, N + 1)]
primes = []

for n in num:
    is_prime = True
    if n == 1: is_prime = False
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime: primes.append(n)

if len(primes):
    print(sum(primes))
    print(min(primes))
else:
    print(-1)