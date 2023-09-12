from collections import deque

def bfs() :
    queue = deque()
    queue.append([0, 0])
    check[0][0] = 1
    while queue :
        col, row = queue.popleft()
        for i in range(4) :
            next_col, next_row = col + dx[i], row + dy[i]
            if next_col < 0 or next_row < 0 or next_col >= n or next_row >= m :
                continue
            if check[next_col][next_row] == 0 and map_[next_col][next_row] != 0:
                check[next_col][next_row] = 1
                map_[next_col][next_row] += map_[col][row]
                queue.append([next_col,next_row])


n, m = map(int, input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
check = [[0 for _ in range(m)] for _ in range(n)]

map_ = []
for i in range(n) :
    map_.append(list(map(int, list(input()))))

bfs()

print(map_[-1][-1])