from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_node) :
    queue = deque()
    queue.append(start_node)
    count = 2
    while queue :
        
        now = queue.popleft()
        for next in path[now] :
            if check[next] == 0 :
                check[next] = count
                count += 1
                queue.append(next)


V, E, R = map(int, input().split())

path = [[]for _ in range(V+1)]
check = [0 for _ in range(V+1)]

for i in range(E) :
    a, b = map(int, input().split())

    path[a].append(b)
    path[b].append(a)

for i in range(1, V+1) :
    path[i].sort()
check[R] = 1
bfs(R)

for i in range(1, V+1) :
    print(check[i])