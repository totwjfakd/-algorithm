import sys

input = sys.stdin.readline

def dfs(node) :
    

    check[node] = 1
    for computer in computer_path[node] :
        if check[computer] == 0 :
            
            dfs(computer)
 



n = int(input())
way_num = int(input())
count = 0
computer_path = [[] for _ in range(n+1)]

check = [0] * (n+1)

for i in range(1, way_num+1) :
    s, e = map(int, input().split())

    computer_path[s].append(e)
    computer_path[e].append(s)

dfs(1)

print(sum(check)-1)