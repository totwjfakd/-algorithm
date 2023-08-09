def dfs(num) :
    if num > n :
        for i in range(1, n+1) :
            if ch[i] == 1 :
                print(i, end = ' ')
        print()
        return
    ch[num] = 1
    dfs(num+1)
    ch[num] = 0
    dfs(num+1)
    

n = int(input())
ch = [0] * (n+1) 
dfs(1)

#상태트리
