from collections import deque

def bfs(start) :
    if start[0] == goal[0] and start[1] == goal[1] :
        return 0
    queue = deque()
    queue.append(start)
 
    while queue :
        col, row = queue.popleft()

        for j in range(8) :
            new_col = col + dx[j]
            new_row = row + dy[j]

            if new_col < 0 or new_row < 0 or new_row >= l or new_col >= l or ch[new_col][new_row] != 0 or (new_col == now[0] and new_row == now[1]):
                continue
            if new_col == goal[0] and new_row == goal[1] :
                return ch[col][row] + 1
            else :
                ch[new_col][new_row] = ch[col][row] + 1
                queue.append([new_col, new_row])

dx, dy = [2, 2, 1, -1, -2, -2, 1, -1], [1, -1, 2, 2, 1, -1, -2, -2]

num = int(input())
for i in range(num) :
    l = int(input())
    now = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    ch = [[0 for _ in range(l)]for _ in range(l)]

    print(bfs(now))

    