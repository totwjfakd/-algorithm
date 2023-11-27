import sys
from collections import deque

def bfs(r, c) :
    queue = deque()
    queue.append([r, c])

    while queue :
        now_r, now_c = queue.popleft()
        for k in range(8) :
            next_r, next_c = now_r+dx[k], now_c+dy[k]

            if next_r < 0 or next_c < 0 or next_r >= h or next_c >= w :
                continue
            if visit[next_r][next_c] == 0 and map_[next_r][next_c] == 1:
                queue.append([next_r, next_c])
                visit[next_r][next_c] = 1

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break

    island_count = 0
    visit = [[0 for _ in range(w)] for _ in range(h)]
    map_ = []

    for i in range(h) :
        map_.append(list(map(int, input().split())))
    
    for i in range(h) :
        for j in range(w) :
            if map_[i][j] == 1 and visit[i][j] == 0 :
                visit[i][j] = 1
                bfs(i, j)
                island_count += 1
    print(island_count)
    
    
