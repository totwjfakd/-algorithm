from collections import deque

def BFS(start) :
    queue = deque()
    queue.append(start)


    while queue :
        now = queue.popleft()

        for next in path[now] :
            
            if ch[next] == 0 and start != next:
                queue.append(next)
                ch[next] = ch[now] + 1

    return sum(ch)


N, M = map(int, input().split())

path = [[] for _ in range(N+1)]

for i in range(M) :
    a, b = map(int, input().split())

    path[a].append(b)
    path[b].append(a)

min_num = 999999
for i in range(1, N+1) :
    ch = [0 for _ in range(N+1)]
    cevin_num = BFS(i)

    if min_num > cevin_num:
        ans = i
        min_num = cevin_num
print(ans)