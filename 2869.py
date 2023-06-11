A, B, V = map(int, input().split())
C = (V - B) / (A - B)
print(int(C) if C == int(C) else int(C) + 1)