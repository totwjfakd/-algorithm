def dfs(node_idx) :
    global count
    if len(path[node_idx]) == 0 and node_idx != root_node:
        count+=1
        return
    elif len(path[node_idx]) == 1 and path[node_idx][0] == del_node :
        count += 1
        return
    for child in path[node_idx] :
        if child != del_node :
            dfs(child)

n = int(input())
node = list(map(int, input().split()))
del_node = int(input())

path = [[] for _ in range(n)]

for i in range(n) :
    if node[i] == -1 :
        root_node = i
    else :
        path[node[i]].append(i)

path[del_node] = []

count = 0
dfs(root_node)

print(count)