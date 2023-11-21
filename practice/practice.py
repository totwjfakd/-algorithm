import sys
from collections import deque

input = sys.stdin.readline

def bfs() :
    queue = deque()
    parent_node = 1
    for node in nodes[parent_node] :
        queue.append([node, parent_node])
    while queue :
        len_queue = len(queue)
        for _ in range(len_queue) :
            child, parent_node = queue.popleft()
            if visit[child] == 0:
                visit[child] = 1
                ans[child] = parent_node
                for n in nodes[child] :
                    if visit[n] == 0 :
                        queue.append([n, child])
n = int(input())

nodes = [[] for i in range(n+1)]
visit = [0 for i in range(n+1)]
visit[1] = 1
ans = [0 for i in range(n+1)]
for i in range(1,n) :
    node1, node2 = map(int, input().split())

    nodes[node1].append(node2)
    nodes[node2].append(node1)

bfs()

for i in range(2, n+1) :
    print(ans[i])