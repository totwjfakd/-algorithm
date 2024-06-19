import sys

def calculate_min_cost(n, w, current_path, visited, current_cost):
    global min_cost
    if len(current_path) == n and w[current_path[-1]][current_path[0]] > 0:
        total_cost = current_cost + w[current_path[-1]][current_path[0]]
        min_cost = min(min_cost, total_cost)
        return
    
    for next_city in range(n):
        if not visited[next_city] and w[current_path[-1]][next_city] > 0:
            visited[next_city] = True
            calculate_min_cost(n, w, current_path + [next_city], visited, current_cost + w[current_path[-1]][next_city])
            visited[next_city] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = sys.maxsize
for i in range(n):
    visit = [False for _ in range(n)]
    visit[i] = True
    calculate_min_cost(n, w, [i], visit, 0)

print(min_cost)
