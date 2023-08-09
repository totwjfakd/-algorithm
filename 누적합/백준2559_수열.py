n, k = map(int, input().split())

arr = list(map(int, input().split()))


maxNum = -999999999
for i in range(1, n) :
    arr[i] += arr[i-1]
for i in range(k-1, n) :
    if i == k-1 :
        if arr[i] > maxNum :
            maxNum = arr[i]
    else :
        if arr[i]-arr[i-k] > maxNum :
            maxNum = arr[i]-arr[i-k]
        
print(maxNum)