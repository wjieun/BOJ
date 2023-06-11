import sys

T = int(input())
for i in range (0, T):
    A, B = map(int, sys.stdin.readline().split())
    A = int(A)
    B = int(B)
    print(A+B)