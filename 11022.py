T = int(input())
for i in range (0, T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))