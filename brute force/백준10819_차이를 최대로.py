def dfs(depth) :
    global max_num
    if depth == n :
        sum_num = 0
        for j in range(n-1) :
            sum_num += abs(new_arr[j] - new_arr[j+1])
        if sum_num > max_num :
            max_num = sum_num
    for i in range(n) :
        if not i in use_idx :
            new_arr.append(arr[i])
            use_idx.append(i)
            dfs(depth+1)
            new_arr.pop()
            use_idx.pop()

n = int(input())

arr = list(map(int, input().split()))
use_idx = []
new_arr = []
max_num = -9999
dfs(0)
print(max_num)
