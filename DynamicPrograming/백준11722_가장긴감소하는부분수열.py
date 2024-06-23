n = int(input())
arr = list(map(int, input().split()))

arr_dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if arr[i] < arr[j] :
            arr_dp[i] = max(arr_dp[i], arr_dp[j] + 1) # 감소하는 조건을 만족하는 부분 수열 중 arr dp 값이 가장 큰 값을 갱신함
print(max(arr_dp))