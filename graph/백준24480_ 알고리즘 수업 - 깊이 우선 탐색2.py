import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(node) :
    global count

    ans[node] = count
    count += 1
    check[node] = 1
    for nv in arr[node] :
        if check[nv] == 0 :

            dfs(nv)


n, m, r = map(int, input().split())

arr = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
count = 1
ans = [0 for _ in range(n+1)]
for i in range(m) :
    s, e = map(int, input().split())
    
    arr[s].append(e)
    arr[e].append(s)
for i in range(1, n+1) :
    arr[i].sort(reverse=True)

# for i in range(n+1) :
#     for j in range(n+1) :
#         print(arr[i][j], end = ' ')
#     print()

dfs(r)
for i in range(1, n+1) :
    print(ans[i])