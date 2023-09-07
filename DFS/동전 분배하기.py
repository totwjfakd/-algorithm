def dfs(depth) :
    global min_num

    if depth == n :
        
        value = max(abc) - min(abc)
        if min_num > value :
            set_arr = set()
            for num in range(3) :
                set_arr.add(abc[num])
            if len(set_arr) == 3 :

                min_num = value
        return
    for i in range(3) :
        abc[i] += arr[depth]
        dfs(depth+1)
        abc[i] -= arr[depth]



n = int(input())

arr = []
visit = [0] * n
for i in range(n) :
    arr.append(int(input()))

abc = [0, 0, 0]
min_num = 99999

dfs(0)
print(min_num)