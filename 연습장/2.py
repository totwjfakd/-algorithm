import sys
sys.setrecursionlimit(2500)

def dfs(node, value):
    global max_dist, farthest_node
    visit[node] = True
    if value > max_dist:
        max_dist = value
        farthest_node = node

    for next_node, weight in tree[node]:
        if not visit[next_node]:
            dfs(next_node, value + weight)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e, v = map(int, input().split())
    tree[s].append((e, v))
    tree[e].append((s, v))

# Step 1: Find the farthest node from an arbitrary node (e.g., node 1)
visit = [False] * (n + 1)
max_dist = 0
farthest_node = 1
dfs(1, 0)

# Step 2: Find the farthest node from the node found in step 1
visit = [False] * (n + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)
