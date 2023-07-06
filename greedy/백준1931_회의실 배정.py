n = int(input())

arr = []

for i in range(n) :
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x:(x[1], x[0]))

et = 0
count = 0
for i in range(n) :
    if arr[i][0] >= et :
        count += 1
        et = arr[i][1]
print(count)