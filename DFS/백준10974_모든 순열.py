def dfs(deep, s) :
    if deep == n :
        print(' '.join(s))
        return
    for i in range(1, n+1) :
        if not str(i) in s :
            s.append(str(i))
            dfs(deep+1, s)
            s.pop()



n = int(input())

dfs(0, [])