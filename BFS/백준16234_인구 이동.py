from collections import deque
import sys

input = sys.stdin.readline

def find_alliance_bfs(start_node) :
    queue = deque()
    queue.append(start_node)

    while queue :
        now_c, now_r = queue.popleft()

        for k in range(4) :
            next_c, next_r = now_c + dx[k], now_r + dy[k]

            if next_c < 0 or next_r < 0 or next_c >= n or next_r >= n :
                continue
            if visit[next_c][next_r] == 0 :
                if abs(map_[now_c][now_r] - map_[next_c][next_r]) >= l and abs(map_[now_c][now_r] - map_[next_c][next_r]) <= r :
                    alliance[alliance_idx].append([next_c, next_r])
                    visit[next_c][next_r] = 1
                    queue.append([next_c, next_r])

def move_population() :
    for alliance_ in alliance :
        if alliance_ :
            alliance_population = 0
            for i in range(len(alliance_)) :
                alliance_population += map_[alliance_[i][0]][alliance_[i][1]]
            for i in range(len(alliance_)) :
                map_[alliance_[i][0]][alliance_[i][1]] = int(alliance_population / len(alliance_))

n, l, r = map(int, input().split())

map_ = []

for i in range(n) :
    map_.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0
while True :
    visit = [[0 for _ in range(n)] for _ in range(n)]
    alliance = [[]for _ in range(n*n)]
    alliance_idx = 0
    for i in range(n) :
        for j in range(n) :
            if visit[i][j] == 0 :
                visit[i][j] = 1
                alliance[alliance_idx].append([i, j])
                find_alliance_bfs([i, j])
                alliance_idx += 1

    print(alliance)
    move_population()

    if alliance_idx == n*n :
        break
    ans += 1

print(ans)