
n = int(input())

arr = []

for i in range(n) :
    arr.append(list(map(int, input().split())))

for i in range(1, n) :
    for j in range(len(arr[i])) :
        if len(arr[i])-1 == j :
            arr[i][j] += arr[i-1][len(arr[i-1])-1]
        elif j == 0 :
            arr[i][j] += arr[i-1][0]
        else :
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[-1]))