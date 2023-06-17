while True:
    n = int(input())
    if n == -1: break
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)

    if sum(divisors) == n:
        print(n, end=' = ')
        for i in range(len(divisors) - 1):
            print(divisors[i], end=' + ')
        print(divisors[len(divisors) - 1])
    else:
        print(n, "is NOT perfect.")