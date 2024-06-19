import sys
from collections import deque

def find_group_bfs(row, col, visit) :

    find_queue = deque()
    find_queue.append((row, col))
    while find_queue :
        now_r, now_c = find_queue.popleft()
        visit[now_r][now_c] = 1

        for i in range(4) :
            next_r, next_c = now_r + dx[i], now_c + dy[i]

            if next_r < 0 or next_c < 0 or next_r >= r or next_c >= c :
                continue
            if map_[next_r][next_c] != 0 and visit[next_r][next_c] == 0 :
                visit[next_r][next_c] = 1
                find_queue.append((next_r, next_c))
    return visit

def bfs() :
    global map_
    count = 0
    while queue :
        queue_len = len(queue)
        changes = {}
        for _ in range(queue_len) :
            now_r, now_c = queue.popleft()
            minus_count = 0
            for j in range(4) :
                next_r, next_c = now_r + dx[j], now_c + dy[j]
                
                if next_r < 0 or next_c < 0 or next_r >= r or next_c >= c :
                    continue
                
                if map_[next_r][next_c] == 0 :
                    minus_count += 1
            new_height = map_[now_r][now_c] - minus_count
            if new_height > 0 :
                queue.append((now_r, now_c))
                changes[(now_r, now_c)] = new_height
            else :
                changes[(now_r, now_c)] = 0
        
        for (i, j), new_height in changes.items():
            map_[i][j] = new_height
        count += 1
        visit = [[0 for _ in range(c)] for _ in range(r)]
        group_count = 0
        for ii, jj in queue :
            if visit[ii][jj] == 0:
                visit = find_group_bfs(ii, jj, visit)
                group_count += 1
        if group_count > 1 :
            print(count)
            exit()

        
input = sys.stdin.readline

r, c = map(int, input().split())

map_ = []

for i in range(r) :
    map_.append(list(map(int, input().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque()

for r_idx in range(r) :
    for c_idx in range(c) :
        if map_[r_idx][c_idx] != 0 :
            queue.append((r_idx, c_idx))

bfs()
print(0)
