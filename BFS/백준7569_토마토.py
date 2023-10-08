from collections import deque
import sys

input = sys.stdin.readline

def bfs() :
    max__ = 1
    while queue :
        now_z, now_y, now_x = queue.popleft()

        for i in range(6) :
            next_z = now_z + dz[i]
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]

            if next_z < 0 or next_y < 0 or next_x < 0 or next_z >= h or next_y >= n or next_x >= m :
                continue

            if visit[next_z][next_y][next_x] == 0 and map_[next_z][next_y][next_x] != -1:
                visit[next_z][next_y][next_x] = 1
                queue.append([next_z, next_y, next_x])
                map_[next_z][next_y][next_x] = map_[now_z][now_y][now_x] + 1
                
                if max__ < map_[now_z][now_y][now_x] + 1 :
                    max__ = map_[now_z][now_y][now_x] + 1
    return max__


m, n, h = map(int, input().split())

map_ = [[] for _ in range(h)]

for i in range(h) :
    for j in range(n) :
        map_[i].append(list(map(int, input().split())))

dx, dy, dz = [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]

queue = deque()
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
# 출발 위치 탐색
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if map_[i][j][k] == 1 :
                queue.append([i, j, k])
                visit[i][j][k] = 1

if len(queue) == 0 : # 모두 다 익어 있을 경우
    ans = 0
else :
    ans = bfs()

# 덜 익은 부분 check
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if map_[i][j][k] == 0 :
                print('-1')
                exit()
print(ans-1)