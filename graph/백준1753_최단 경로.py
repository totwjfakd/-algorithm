import heapq
import sys
input = sys.stdin.readline
def dijkstra(start_node):
    min_path = [float('inf')] * (V + 1)
    min_path[start_node] = 0
    
    pq = []
    heapq.heappush(pq, (0, start_node))
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > min_path[current_node]:
            continue
        
        for next_node, weight in path[current_node]:
            if current_dist + weight < min_path[next_node]:
                min_path[next_node] = current_dist + weight
                heapq.heappush(pq, (min_path[next_node], next_node))
    
    return min_path

V, E = map(int, input().split())
start_node = int(input())

path = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    path[u].append((v, w))

min_path = dijkstra(start_node)

for i in range(1, V + 1):
    if min_path[i] == float('inf'):
        print('INF')
    else:
        print(min_path[i])

# 다익스트라 알고리즘 공부하고 다시 풀어볼 것