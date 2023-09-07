def dfs(depth, start) :
    global c
    if depth == m :
        for i in range(m) :
            print(res[i], end = ' ')
        print()
        c+=1
        return
    for j in range(start, n+1) :


        res[depth] = j
        dfs(depth+1, j+1)


n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
res = [0] * m

c = 0

dfs(0, 1)
print(c)