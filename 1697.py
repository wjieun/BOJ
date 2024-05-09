from queue import Queue

N, K = list(map(int, input().split()))
min_time = 1000000

def move(X, action):
    if action == 0:
        return X - 1
    elif action == 1:
        return X + 1
    elif action == 2:
        return X * 2

def bfs():
    global N, K, min_time
    frontier = Queue()

    if N == K:
        min_time = 0
        return 0

    frontier.put([N, -1, 0])
    explored = set()

    while not frontier.empty():
        now_N = frontier.get()

        for action in range(3):
            new_N = move(now_N[0], action)
            new_N_cost = now_N[2] + 1

            if new_N == K:
                if min_time > new_N_cost:
                    min_time = new_N_cost
                continue

            if new_N >= 0 and new_N <= 100000 and new_N not in explored:
                frontier.put([new_N, action, new_N_cost])
                explored.add(new_N)

bfs()
print(min_time)