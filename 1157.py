Input = input().upper()
words = list(set(Input))
c = []

for i in words:
    c.append(Input.count(i))

if c.count(max(c)) > 1:
    print('?')
else:
    ind = c.index(max(c))
    print(words[ind])