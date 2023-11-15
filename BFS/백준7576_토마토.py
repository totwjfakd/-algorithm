from collections import deque
import sys
input = sys.stdin.readline

def bfs() :

    while queue :
        y, x = queue.popleft()
        
        for i in range(4) :
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m or map_[next_y][next_x] == -1:
                continue
            else :
                if visit[next_y][next_x] == 0 :
                    visit[next_y][next_x] = 1
                    queue.append([next_y,next_x])
                    map_[next_y][next_x] = map_[y][x] + 1

n, m = map(int, input().split())
map_ = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for i in range(m) :
    map_.append(list(map(int, input().split())))

visit = [[0 for _ in range(n+1)]for _ in range(m+1)]

queue = deque()
for i in range(m) :
    for j in range(n) :
        if map_[i][j] == 1 :
            queue.append([i, j])
            map_[i][j] = 0
            
for i, j in queue :
    visit[i][j] = 1
bfs()
max_num = 0

for i in range(m) :
    if max(map_[i]) > max_num :
        max_num = max(map_[i])
    print(map_[i])
for i in range(m) :
    for j in range(n) :
        if visit[i][j] == 0 and map_[i][j] == 0 :
            print(-1)
            exit()
else :
    print(max_num)