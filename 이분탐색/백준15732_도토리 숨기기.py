import sys

input = sys.stdin.readline



N, K, D = map(int, input().split())
rules = []

for i in range(K) :
    rules.append(list(map(int, input().split())))

lt, rt = 1, N
ans = 0
while lt <= rt :
    mid = (lt + rt) // 2
    cnt = 0
    for s, e, step in rules :
        if s > mid :
            continue
        if mid > e :
            cnt += (e-s) // step + 1
        else :
            cnt += (mid-s) // step + 1
        
        if cnt >= D :
            rt = mid-1
            ans = mid
            break     
    else :
        lt = mid+1
print(ans)