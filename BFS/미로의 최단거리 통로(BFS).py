from collections import deque

def bfs() :
    queue = deque()
    queue.append([0, 0])

    while queue :
        now_x, now_y = queue.popleft()
        for i in range(4) :
            next_x, next_y = now_x + dx[i], now_y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= 7 or next_y >= 7 or map_[next_x][next_y] == 1 :
                continue
            if visit[next_x][next_y] == 0 :
                visit[next_x][next_y] = visit[now_x][now_y] + 1
                queue.append([next_x, next_y])


map_ = []
visit = [[0 for _ in range(7)] for _ in range(7)]
for i in range(7) :
    map_.append(list(map(int, input().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

bfs()

if visit[6][6] == 0 :
    print(-1)
else :
    print(visit[6][6])