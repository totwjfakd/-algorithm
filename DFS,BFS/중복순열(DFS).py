def dfs(deep, A) :
    if deep == m :
        print(' '.join(A))
        return
    for i in range(1, n+1) :
        A.append(str(i))
        dfs(deep+1, A)
        A.pop()




n, m = map(int, input().split())
arr = []


dfs(0, [])