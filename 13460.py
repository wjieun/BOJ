N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))

B_index = (0, 0)
R_index = (0, 0)
O_index = (0, 0)

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B': B_index = (i, j)
        elif board[i][j] == 'R': R_index = (i, j)
        elif board[i][j] == 'O': O_index = (i, j)




