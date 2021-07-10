num1, num2 = map(int, input().split())

array = []
for i in range(num1) :
    array.append(int(input()))

rt = max(array)
lt = 1
k = 0

while lt<=rt :
    mid = (lt+rt) // 2
    for i in range(num1) :
        k+= array[i] // mid

    if  k < num2:
        rt = mid - 1
    else  :
        lt = mid + 1
        res = mid
    k = 0

print(res)