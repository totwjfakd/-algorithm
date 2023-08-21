def dfs(deep, A, mid) :
    if deep == n :
        return
    
    if len(A) == 1 :
        ans[deep].append(A[0])
    else :
        ans[deep].append(A[mid])
    
    dfs(deep+1, A[:mid], len(A[:mid])//2)
    dfs(deep+1, A[mid+1:], len(A[:mid])//2)


n = int(input())

arr = input().split()

mid = len(arr) // 2
ans = [[] for _ in range(n)]
dfs(0, arr, mid)

for array in ans :
    print(' '.join(array))