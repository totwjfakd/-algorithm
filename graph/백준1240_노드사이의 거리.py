import sys

input = sys.stdin.readline


def dfs(start_node, value) :
    global min_path
    if start_node == find_node :
        if min_path > value :
            min_path = value
        return
    for node in path[start_node] :
        #print(node)
        if check[node[0]] == 0 :
            check[node[0]] = 1
            dfs(node[0], value+node[1])
            check[node[0]] = 0
N, M = map(int, input().split())

path = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
for i in range(N-1) :
    s, e, v = map(int, input().split())
    path[s].append((e, v))
    path[e].append((s, v))
for i in range(M) :
    min_path = float('inf')
    a, find_node = map(int, input().split())
    dfs(a, 0)
    print(min_path)
