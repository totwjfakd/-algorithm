import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(m) :
    arr.append(int(input()))

lt = 1
rt = max(arr)
ans = (lt+rt) // 2
while lt <= rt :
    mid = (lt+rt) // 2
    total = 0

    for i in range(m) :
        if arr[i] % mid == 0 :
            total += arr[i] // mid
        else :
            total += (arr[i] // mid) + 1
    if total > n :
        lt = mid + 1
    else :
        rt = mid - 1
print(lt)

