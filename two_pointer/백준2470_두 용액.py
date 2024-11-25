n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lt = 0
rt = len(arr)-1

num1, num2 = arr[0], arr[-1]
min_num = 2000000001
while lt < rt:
    now_num = abs(arr[lt] + arr[rt])

    if min_num > now_num :
        min_num = now_num
        num1, num2 = arr[lt], arr[rt]
    
    if abs(arr[lt+1] + arr[rt]) > abs(arr[lt] + arr[rt-1]) :
        rt -= 1
    else :
        lt += 1
    
print(num1, num2)
