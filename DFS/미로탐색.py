def dfs(now_c, now_r) :
    global count
        
    if now_c == 6 and now_r == 6 :
        count += 1
        return
    
    for dt in range(4) :
        next_c, next_r = now_c + dx[dt], now_r + dy[dt]
        if next_c < 0 or next_r < 0 or next_c > 6 or next_r > 6 :
            continue
        if visit[next_c][next_r] == 0 and map_[next_c][next_r] == 0:
            
            visit[next_c][next_r] = 1
            dfs(next_c, next_r)
            visit[next_c][next_r] = 0



map_ = []
visit = [[0 for _ in range(7)] for _ in range(7)]

count = 0
visit[0][0] = 1
for i in range(7) :
    map_.append(list(map(int, input().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

dfs(0,0)
print(count)