X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 != 0:
    a = line + 1 - X
    b = X
else:
    a = X
    b = line + 1 - X

print(a, '/', b, sep='')