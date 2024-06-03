import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))

lt = 1
rt = sum(arr)
k = 10000
while lt <= rt :
    mid = (lt+rt) // 2
    money = mid
    cnt = 1

    for num in arr :
        if money < num :
            cnt += 1
            money = mid
        money -= num
    
    if cnt > m or mid < max(arr):
        lt = mid + 1
    else :
        rt = mid - 1
        k = mid


print(k)
