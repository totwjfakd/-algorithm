n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_num = -9999999

for i in range(1, n) :
    arr[i] = arr[i-1] + arr[i]

for i in range(m-1, n) :
    print(i)
    if i-(m-1) == 0 :
        sum_num = arr[i]
    else :
        sum_num = arr[i] - arr[i-(m-1)-1]

    if max_num < sum_num :
        max_num = sum_num


print(max_num)
