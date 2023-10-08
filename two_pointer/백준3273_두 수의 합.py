n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

lt = 0
rt = len(arr)-1
count = 0
while lt<rt :
    s = arr[lt] + arr[rt]

    if s > x :
        rt -= 1
    elif s < x :
        lt += 1
    else :
        count += 1
        lt += 1

print(count)
