def dfs(sumN, depth) :
    if check[sumN] == 0 and sumN > 0 :
        check[sumN] = 1
    
    if depth == num :
        return
    if sumN > sum(arr) :
        return

    dfs(sumN+arr[depth], depth+1)
    dfs(sumN-arr[depth], depth+1)
    dfs(sumN, depth+1)

num = int(input())
arr = list(map(int, input().split()))
check = [0 for _ in range(0, sum(arr)+1)]

dfs(0, 0)

count = -1

for n in check :
    if n == 0 :
        count += 1

print(count)