num, find_num = map(int, input().split())

a = list(map(int, input().split()))

a.sort()
print(a, num, find_num)
lt = 0
rt = num-1
while lt<=rt : 
    mid = (lt+rt)//2

    if a[mid] == find_num :
        break

    elif a[mid] > find_num :
        rt = mid-1
    else:
        lt = mid+1

print(mid + 1)