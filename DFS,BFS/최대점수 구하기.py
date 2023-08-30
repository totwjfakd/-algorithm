def dfs(sum_score, sum_time, depth) :
    global max_num

    if sum_time > limit_time :
        return
    if depth == N :
        if sum_score > max_num :
            
            max_num = sum_score
        return


    dfs(sum_score+arr[depth][0], sum_time+arr[depth][1], depth+1)
    dfs(sum_score, sum_time, depth+1)

N, limit_time = map(int, input().split())

arr = []
check = [0] * N
for i in range(N) :
    arr.append(list(map(int, input().split())))

max_num = -99999

dfs(0, 0, 0)
print(max_num)
