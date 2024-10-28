max_ = 0

def dfs(d, m):
    global max_
    if d == n+1:
        if max_ < m :
            max_ = m
    if d > n : return
    
    dfs(d+arr[d][0], m+arr[d][1])
    dfs(d+1, m)

n = int(input())
arr = [None]
for i in range(n):
    arr.append(list(map(int, input().split())))

dfs(1, 0)

print(max_)