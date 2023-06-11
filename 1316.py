N = int(input())
c = N
for i in range(N):
    w = input()
    for j in range(len(w)-1):
        if w[j] != w[j+1] and w[j] in w[j+1:]:
                c -= 1
                break
print(c)