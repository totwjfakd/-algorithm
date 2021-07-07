def get_num(m, k) :
    len_num = 0
    global array
    for i in range(k) :
        len_num += array[i] // m

    return len_num
    


k, n = map(int, input().split())

array = []
for i in range(k) :
    array.append(int(input()))

lt = 1
rt = max(array)

while lt <= rt :
    mid = (lt+rt) // 2
    print(mid)
    len_n = get_num(mid, k)
    
    if len_n >= n :
        
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1

print(res)
    