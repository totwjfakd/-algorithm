def dfs(deepth, n, s) :
    if deepth == m :
        print(' '.join(s))

    else :
        for i in range(1, n+1, 1) :
            if not str(i) in s :
                if deepth >= 1 and int(s[-1]) < i :
                    s.append(str(i))
                    dfs(deepth+1, n, s)
                    s.pop()
                elif deepth == 0 :
                    s.append(str(i))
                    dfs(deepth+1, n, s)
                    s.pop()

    
n, m = map(int, input().split())
ans = []
dfs(0, n, ans)