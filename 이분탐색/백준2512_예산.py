n = int(input())

arr = list(map(int, input().split()))

money = int(input())

lt = 1
rt = max(arr)
ans = 0

while lt <= rt :
    mid = (lt+rt) // 2

    sum_ = 0

    for num in arr :
        if num < mid :
            sum_ += num
        else :
            sum_ += mid
        if sum_ > money :
            rt = mid - 1
            break
    else :
        if max(arr) < mid :
            rt = mid - 1
        else :
            lt = mid + 1
        ans = mid
print(ans)