from collections import deque
import sys
input = sys.stdin.readline

def dfs(node, depth) :
    res.append(str(node))
    
    for next in path[node] :
        if check[next] == 0 :
            check[next] = 1
            dfs(next, depth+1)

def bfs(start) :
    queue = deque()
    queue.append(start)
    res.append(str(start))
    while queue :
        now = queue.popleft()
        for next in path[now] :
            if check[next] == 0 :
                check[next] = 1
                res.append(str(next))
                queue.append(next)
    
n, m, start_node = map(int, input().split())

path = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
for i in range(m) :
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

for i in range(1, n+1) :
    path[i].sort()
res = []
check = [0 for _ in range(n+1)]

check[start_node] = 1

dfs(start_node, 1)
print(' '.join(res))

res = []
check = [0 for _ in range(n+1)]
check[start_node] = 1
bfs(start_node)
print(' '.join(res))