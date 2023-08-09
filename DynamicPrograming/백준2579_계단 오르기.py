import sys
n = int(input())

arr = []
dp = []
for i in range(n) :
    arr.append(int(sys.stdin.readline().rstrip()))

if n == 1 :
    print(arr[0])
    exit()
if n == 2 :
    print(arr[0]+arr[1])
    exit()
if n == 3 :
    print(max(arr[0]+arr[2], arr[1]+arr[2]))
    exit()
dp.append(arr[0]) 
dp.append(arr[0]+arr[1])
dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3, n, 1) :
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])) 

print(dp[n-1])