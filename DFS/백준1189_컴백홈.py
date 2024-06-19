import sys

input = sys.stdin.readline

def dfs(n, row, col, visit):
    global count
    if n >= k :
        if row == 0 and col == c-1 :
            count += 1
        return

    for i in range(4) :
        next_row, next_col = row + dx[i], col + dy[i]
        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c :
            continue
        if not visit[next_row][next_col] and map_[next_row][next_col] == '.':
            visit[next_row][next_col] = True
            dfs(n+1, next_row, next_col, visit)
            visit[next_row][next_col] = False

r, c, k = map(int, input().split())
map_ = []
for i in range(r): 
    map_.append(list(input()))

count = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visit = [[False for _ in range(c)] for _ in range(r)]
visit[r-1][0] = True

dfs(1, r-1, 0, visit)
print(count)
