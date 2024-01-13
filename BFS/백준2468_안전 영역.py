import sys
from collections import deque
def bfs() :

    while queue :
        now_c, now_r = queue.popleft()
            
        for dt in range(4) :
            next_c, next_r = now_c + dx[dt], now_r + dy[dt]
            
            if next_c < 0 or next_r < 0 or next_c >= n or next_r >= n :
                continue
            if rain_map_visit[next_c][next_r] == 0 :
                rain_map_visit[next_c][next_r] = 2
                queue.append((next_c, next_r))

input = sys.stdin.readline

n = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
map_ = []
ans = 0
for i in range(n) :
    map_.append(list(map(int, input().split())))
for i in range(0, 101) :
    rain_map_visit = [[0 for _ in range(n)] for _ in range(n)]
    
    count = 0
    safe_area = []
    for j in range(n) :
        for k in range(n) :
            if map_[j][k] <= i :
                rain_map_visit[j][k] = 1
            else :
                safe_area.append((j, k))
    for c, r in safe_area :
        queue = deque()
        
        if rain_map_visit[c][r] == 0 :
            count += 1
            rain_map_visit[c][r] = 2
            queue.append((c, r))
            bfs()
    if ans < count :
        ans = count

print(ans)