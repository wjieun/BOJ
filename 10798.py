arr = []
arr_len = []

for _ in range(5):
    L = list(input())
    arr.append(L)
    arr_len.append(len(L))

for i in range(max(arr_len)):
    for j in range(5):
        if arr_len[j] > i:
            print(arr[j][i], end='')