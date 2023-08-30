import sys

def dfs(c, r) :
    global count
    if c < 0 or c >= num or r < 0 or r >= num :
        return
    if arr[c][r] == '1' and check_arr[c][r] == 0:
        count += 1
        check_arr[c][r] = 1
        for k in range(4) :
            dfs(c+dx[k], r+dy[k])
        return count
    


num = int(input())
check_arr = [[0 for _ in range(num)] for _ in range(num)]
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(num) :
    arr.append(input())

ans = []

for i in range(0, num) :
    for j in range(0, num) :
        if check_arr[i][j] == 0 and arr[i][j] == '1':
            count = 0
            ans.append(dfs(i, j))
print(len(ans))
ans.sort()
for n in ans :
    print(n)