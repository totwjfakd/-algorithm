import copy
def dfs(deep) :
    if deep == n :
        ans = 0
        for i in range(n) :
            ans += res[i] * b[i]
        if ans == f :
            for num in res :
                print(num, end = ' ')
            print()
            exit()
    
    for i in range(1, n+1) :
        if ch[i] == 0 :
            ch[i] = 1
            res[deep] = i
            dfs(deep+1)
            ch[i] = 0


n, f = map(int, input().split())

ch = [0] * (n+1)
res = [0] * n
b = [1]*n
for i in range(1, n) :
    b[i] = b[i-1] * (n-i) // i


dfs(0)
