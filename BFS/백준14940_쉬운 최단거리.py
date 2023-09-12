from collections import deque
import sys
input = sys.stdin.readline

def bfs(index) :
    queue = deque()
    queue.append(index)

    visit[index[0]][index[1]] = 1

    while queue :
        y, x = queue.popleft()
        for i in range(4) :
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or map_[new_y][new_x] == 0:
                continue
            else :
                if visit[new_y][new_x] == 0 :
                    visit[new_y][new_x] = 1
                    ans[new_y][new_x] = ans[y][x]+1
                    queue.append([new_y, new_x])

n, m = map(int, input().split())

map_ = []
for i in range(n) :
    map_.append(list(map(int, input().split())))

ans = [[0 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

is_break = False
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
for i in range(n) :
    for j in range(m) :
        if map_[i][j] == 2 :
            start_idx = [i, j]

            is_break = True
            break
    if is_break :
        break

bfs(start_idx)


for i in range(n) :
    for j in range(m) :
        if map_[i][j] == 1 and visit[i][j] == 0 :
            ans[i][j] = -1
            

for i in range(n) :
    for j in range(m) :
        print(ans[i][j], end = ' ')
    print()