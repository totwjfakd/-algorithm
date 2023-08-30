n = int(input())


arr = [0, 1, 1, 2]

if n <= 3 :
    print(arr[n])
else :
    for i in range(4, n+1) :
        arr.append((arr[i-2] + arr[i-1]) % 1000000007)
    print(arr[n])