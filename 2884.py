H, M = input().split()
H = int(H)
M = int(M)

if M >= 45: print(H, M-45)
else: print((H+24-1)%24, 60-(45-M))