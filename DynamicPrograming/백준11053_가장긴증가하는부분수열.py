n = int(input())
arr = list(map(int, input().split()))

arr_dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if arr[i] > arr[j] :
            arr_dp[i] = max(arr_dp[i], arr_dp[j] + 1)
print(max(arr_dp))