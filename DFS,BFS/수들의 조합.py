def dfs(depth, start) :
    global c
    if depth == m : 
        if sum(res) % num == 0 :
            c+=1
        return
    for j in range(start, n) :
        res[depth] = nums[j]
        dfs(depth+1, j+1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
num = int(input())

res = [0] * m

c = 0
dfs(0, 0)
print(c)