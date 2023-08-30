def dfs(depth, s) :
    if depth == m :
        for i in range(m) :
            print(res[i], end = ' ')
        print()
        return
    
    remember = 0

    for i in range(s, n) :
        if remember != arr[i] :
            remember = arr[i]
            res[depth] = arr[i]
            dfs(depth+1, i)

    

n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

res = [0] * m

dfs(0, 0)