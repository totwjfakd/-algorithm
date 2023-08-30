def dfs(depth, start, res) :
    global count
    if res[-1] == n :
        for i in range(depth+1) :
            print(res[i], end = ' ')
        print()

        count += 1
        return
    for i in range(2, n+1) :
        if arr[start][i] == 1 :
            if check[i] == 0 :
                check[i] = 1
                res.append(i)
                dfs(depth+1, i, res)
                res.pop()
                check[i] = 0
        

n, m = map(int, input().split())

arr = [[0 for _ in range(m+1)] for _ in range(m+1)]

check = [0 for _ in range(n+1)]
count = 0
check[1] = 1
for i in range(m) :
    s, e = map(int, input().split())

    arr[s][e] = 1

for i in range(n) :
    for j in range(n) :
        print(arr[i+1][j+1], end = ' ')
    print()

dfs(0, 1, [1])
print(count)