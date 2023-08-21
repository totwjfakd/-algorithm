def dfs(deep, sum) :
    global max_kg, maxN
    if deep > n-1 :
        if maxN < sum and sum < max_kg:
            maxN = sum
        return
    dfs(deep+1, sum+arr[deep])
    dfs(deep+1, sum)


max_kg, n = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))
maxN = -1
dfs(0, 0)
print(maxN)