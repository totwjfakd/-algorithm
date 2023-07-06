

n, c = map(int, input().split())
arr = []

for i in range(n) :
    arr.append(int(input()))
arr.sort()

lt = 1
rt = arr[-1]

while lt <= rt :
    mid = (lt+rt)//2
    count = 1
    last_cow_point = arr[0]
    for i in range(1, n) :
        if arr[i] - last_cow_point >= mid :
            last_cow_point = arr[i]
            count += 1

    if count >= c :
        res = mid 
        lt = mid + 1
    else :
        rt = mid - 1

print(res)