import sys
def dfs(deep, x_idx, y_idx) :
    global maxx

    maxx = max(maxx, deep)
    for i in range(4) :
        x = x_idx + dx[i]
        y = y_idx + dy[i]
        if (x >= 0 and x < c and y >= 0 and y < r) and not pass_list[ord(arr[y][x])-65] :
            pass_list[ord(arr[y][x])-65] = True
            dfs(deep+1, x, y)
            pass_list[ord(arr[y][x])-65] = False

        
maxx = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
r, c = map(int, input().split())

arr = []
for _ in range(r) :
    arr.append(sys.stdin.readline().rstrip())

pass_list = [False]*26

pass_list[ord(arr[0][0])-65] = True
dfs(1, 0, 0)
print(maxx)