a, b = input().split()
a = int(a)
b = int(b)
c = int(input())

h = c // 60
m = c % 60


if b + m >= 60:
    h += (b + m) // 60
    m = (b + m) % 60
else:
    m += b

if a + h >= 24:
    h = (a + h) % 24
else:
    h += a

print(h, m)