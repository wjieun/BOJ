T = int(input())
for i in range(0, T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='')
    print()