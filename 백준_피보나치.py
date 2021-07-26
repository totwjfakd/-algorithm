

array = [[1, 0], [0, 1]]
for i in range(2, 41) :
    new_arr = [array[i-2][0]+array[i-1][0], array[i-2][1]+array[i-1][1]]
    array.append(new_arr)


c = int(input())

for i in range(c) :
    num = int(input())

    
    print(array[num][0], array[num][1])
    
