arr = []
for _ in range(9):
    L = list(map(int, input().split()))
    arr.append(L)

row_arr = []
for a in arr:
    row_arr.append(max(a))
max_row = max(range(len(row_arr)), key=lambda i: row_arr[i])
max_col = max(range(len(arr[max_row])), key=lambda i: arr[max_row][i])

print(max(row_arr))
print(max_row + 1, max_col + 1)