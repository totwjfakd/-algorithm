from collections import deque

def bfs(start) :
    global ans
    check[start[0]][start[1]] = 1
    ans += map_[start[0]][start[1]]
    queue = deque()
    queue.append(start)
    c = 0
    while queue :
        que_len = len(queue)
        c+=1 # BFS 깊이 카운팅
        for _ in range(que_len) : # BFS깊이를 알기 위해 반복문 추가, 현제 Queue에 들어있는 만큼만 뽑아옴

            now_col, now_row = queue.popleft()
                
            for i in range(4) :
                next_col, next_row = now_col + dx[i], now_row + dy[i]

                if next_col < 0 or next_row < 0 or next_col >= num or next_row >= num :
                    continue
                if check[next_col][next_row] == 0 :
                    if c < num // 2 :
                        queue.append([next_col,next_row])
                    check[next_col][next_row] = 1
                    ans += map_[next_col][next_row]

        

num = int(input())
map_ = []
check = [[0 for _ in range(num)] for _ in range(num)]
for i in range(num) :
    map_.append(list(map(int, input().split())))


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

ans = 0

bfs([num//2, num//2])

print(ans)