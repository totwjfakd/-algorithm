def dfs(deep) :
    global cnt
    if deep == m :
        cnt += 1
        for j in range(m) :
            print(res[j], end = ' ')
        print()
        return
    for j in range(1, n+1) :
        if ch[j] == 0 :
            ch[j] = 1
            res[deep] = j
            dfs(deep+1)
            ch[j] = 0

n, m = map(int, input().split()) 

cnt = 0
res = [0] * m
ch = [0] * (n+1)
dfs(0)