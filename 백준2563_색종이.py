
n = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]
count = 0
for i in range(n) :
    x, y = map(int, input().split())

    for j in range(10) :
        for k in range(10) :
            arr[x-1+j][y-1+k] = 1
for i in range(100) :
    for j in range(100) :
        if arr[i][j] == 1 :
            count += 1

print(count)

