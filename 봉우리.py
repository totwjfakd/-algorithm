num = int(input())

array = [list(map(int, input().split()))for _ in range(num)]

for i in range(num) :
    array[i].insert(0, 0)
    array[i].append(0)


array.insert(0, [0]*(num+2))
array.append([0]*(num+2))

for i in range(num+2) :
    print(array[i])

res = 0
for i in range(1, num+1) :
    for j in range(1, num+1) :
        if array[i][j] > array[i-1][j] and array[i][j] > array[i][j-1] and array[i][j] > array[i+1][j] and array[i][j] > array[i][j+1] :
            print(i, j)
            res += 1
print (res)
