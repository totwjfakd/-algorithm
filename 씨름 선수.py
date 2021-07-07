n = int(input())

array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

cnt = 0
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        if array[i][0] == 0 :
            break
        if array[j][0] == 0 :
            continue
        if array[i][0] > array[j][0] or array[i][1] > array[j][1] :
            continue
        else :
            array[i][0] = 0
            break

for i in range(n) :
    if array[i][0] != 0:
        cnt += 1

print(cnt)

