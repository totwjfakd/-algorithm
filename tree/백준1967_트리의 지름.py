import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(node, value) :
    global ans, start_node

    if ans < value :
        ans = value
        start_node = node
    visit[node] = True
    for j in range(len(tree[node])) :
        if visit[tree[node][j][0]] == False :
            dfs(tree[node][j][0], value+tree[node][j][1])
        

n = int(input())
if n==1 :
    print("0")
    exit()
tree = [[] for _ in range(n+1)]

for i in range(n-1) :
    s, e, v = map(int, input().split())

    tree[s].append([e, v])
    tree[e].append([s, v])

ans = 0

visit = [False for _ in range(n+1)]
start_node = None
dfs(1, 0)

ans = 0
visit = [False for _ in range(n+1)]
dfs(start_node, 0)

print(ans)