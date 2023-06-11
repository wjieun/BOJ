dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
Input = input()
time = 0
for i in Input:
    for j in dial:
        if i in j:
            time += dial.index(j) + 2 + 1
            break
print(time)