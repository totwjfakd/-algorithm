n = int(input())
arr_move_cost = list(map(int, input().split()))
arr_city = list(map(int, input().split()))

min_cost = 1000000001

ans = 0
i=0
for k in range(n-1) :
    if arr_city[k] < min_cost :
        min_cost = arr_city[k]
        min_idx = k
    ans += min_cost * arr_move_cost[i]
        
    i+=1
print(ans)