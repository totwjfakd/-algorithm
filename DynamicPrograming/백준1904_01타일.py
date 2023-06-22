n = int(input())
arr = [0 for i in range(1000001)]
arr[0], arr[1] = 1, 1

for i in range(2, 1000001, 1) :
    arr[i] = (arr[i-1] + arr[i-2])%15746

print(arr[n])