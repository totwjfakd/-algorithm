from itertools import combinations as cmb
from collections import deque
import sys
import copy

input = sys.stdin.readline

def bfs() :
    global max_num
    while p_virus_idx :
        now = p_virus_idx.popleft()
        now_c, now_r = now[0], now[1]

        for k in range(4) :
            next_c, next_r = now_c + dx[k], now_r + dy[k]
            if next_c < 0 or next_r < 0 or next_c >= n or next_r >= m :
                continue
            if p_map_[next_c][next_r] == 0 :
                p_map_[next_c][next_r] = 2
                p_virus_idx.append([next_c, next_r])
    count = 0
    for w in range(n) :
        for q in range(m) :
            if p_map_[w][q] == 0 :
                count += 1

    return count

n, m = map(int, input().split())
map_ = []
for i in range(n) :
    map_.append(list(map(int, input().split())))

zero_idx = []
virus_idx = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(n) :
    for j in range(m) :
        if map_[i][j] == 0 :
            zero_idx.append([i, j])
        elif map_[i][j] == 2 :
            virus_idx.append([i, j])

cmb_zero_idx = list(cmb(zero_idx, 3))
max_num = 0
for i in range(len(cmb_zero_idx)) :
    p_map_ = copy.deepcopy(map_)
    p_virus_idx = deque(copy.deepcopy(virus_idx))
    for j in range(3) :
        c, r = cmb_zero_idx[i][j][0], cmb_zero_idx[i][j][1]
        p_map_[c][r] = 1
    zero_count = bfs()
    if max_num < zero_count :
        max_num = zero_count

print(max_num)