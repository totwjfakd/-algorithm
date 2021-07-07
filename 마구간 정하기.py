
def is_possible(mid) :
    global c
    global input_list
    num = c
    print(mid, "!!!!!")
    for i in range(len(input_list)) :
        if i == 0 :
            num -= 1
            last = input_list[i]
            continue
        
        if input_list[i]-last >= mid :
            num -= 1
            last = input_list[i]
    if num <= 0 :
        return True
    return False
        


n, c = map(int, input().split())

array = [0] * (n+1)
input_list = []
for i in range(n) :
    input_list.append(int(input()))
input_list.sort()

lt = 1
rt = input_list[-1]
res = 0
while lt <= rt :
    mid = (lt+rt) // 2
    if is_possible(mid) :
        res = mid
        lt = mid + 1
    else :
        
        rt = mid - 1


print (res)