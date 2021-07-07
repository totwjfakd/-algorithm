num = int(input())

array = [list(map(int, input().split())) for _ in range(num)]

max_num = -999999
sum_value1 = 0
sum_value2 = 0
sum_value3 = 0
sum_value4 = 0
for i in range(num) :
    sum_value1 = 0
    sum_value2 = 0

    for j in range(num) :
        sum_value1 += array[i][j]
        sum_value2 += array[j][i]
        if i+j == num-1 :
            sum_value4 += array[i][j]
    sum_value3 += array[i][i]
    
    if sum_value1 > max_num :
        max_num = sum_value1
    if sum_value2 > max_num :
        max_num = sum_value2

if sum_value3 > max_num :
    max_num = sum_value3
if sum_value4 > max_num :
    max_num = sum_value4

print(max_num)
