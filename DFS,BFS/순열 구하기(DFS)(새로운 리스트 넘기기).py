def dfs(deep, Arr, new_arr) :
    global c
    if deep == m :
        c+=1
        print(' '.join(new_arr))
        return
    for i in range(len(Arr)) :
        new_arr.append(Arr[i])

        dfs(deep+1, Arr[:i]+Arr[i+1:], new_arr)
        new_arr.pop()

n, m = map(int, input().split())
c = 0
arr = []

for i in range(n) :
    arr.append(str(i+1))

dfs(0, arr, [])
print(c)