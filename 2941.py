alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
Input = input()
c = len(Input)
for i in alphabet:
    c -= Input.count(i)
c -= Input.count('dz=')
print(c)