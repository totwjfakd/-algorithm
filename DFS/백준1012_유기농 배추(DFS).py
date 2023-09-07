import sys
sys.setrecursionlimit(10000) 

def dfs(x2, y2) :
    if x2 <= -1 or x2 >= m or y2 <= -1 or y2 >= n :
        return False
    if arr[x2][y2] == 1 :
        arr[x2][y2] = 0
        dfs(x2-1, y2)
        dfs(x2+1, y2)
        dfs(x2, y2-1)
        dfs(x2, y2+1)
        return True
    return False

t = int(sys.stdin.readline().rstrip())
for i in range(t) :
    ans = 0
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]
    for j in range(k) :
        x, y = map(int, sys.stdin.readline().rstrip().split())
        arr[x][y] = 1

    for j in range(n) :
        for k in range(m) :
            if dfs(k,j) :
                ans += 1
    
    print(ans)
