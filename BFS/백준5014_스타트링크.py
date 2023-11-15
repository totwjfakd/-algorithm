from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()

queue.append([S, 0])

visit = [0]*1000001
visit[S] = 1

ans = []

while queue :
    now_floor, now_count = queue.popleft()

    if now_floor == G :
        ans.append(now_count)
    
    next_floor_up = now_floor + U
    next_floor_down = now_floor - D
    
    if next_floor_down >= 1 and next_floor_down <=F and visit[next_floor_down] == 0 :
        queue.append([next_floor_down, now_count+1])
        visit[next_floor_down] = 1
    if next_floor_up >= 1 and next_floor_up <= F and visit[next_floor_up] == 0 :
        queue.append([next_floor_up, now_count+1])
        visit[next_floor_up] = 1
if ans :
    print(min(ans))
else :
    print("use the stairs")

