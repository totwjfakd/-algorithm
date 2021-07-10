def get_len(arr, m) :
    num = 0
    for i in range(len(arr)) :
        a = arr[i]-m
        if a < 0 :
            num += 0
        else :
            num += a
    return num

n, m = map(int, input().split())
array = list(map(int, input().split()))

rt = max(array)
lt = 1
m2 = (lt+rt)//2
res = get_len(array, m2)

while lt <= rt :
    mid = (lt+rt)//2

    tree_len = get_len(array, mid)
    if tree_len < m :
        rt = mid - 1

    else :
        lt = mid + 1
        if tree_len == m :
            res = mid
print(res)
