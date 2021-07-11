import sys
def get_len(arr, m) :
    num = 0
    for i in range(len(arr)) :
        a = arr[i]-m
        if a < 0 :
            num += 0
        else :
            num += a
    return num

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

rt = max(array)
lt = 1
res = 0

while lt <= rt :
    mid = (lt+rt)//2

    tree_len = get_len(array, mid)
    if tree_len < m :
        rt = mid - 1

    else :
        lt = mid + 1
        res = mid
print(res)
