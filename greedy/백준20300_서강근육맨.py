n = int(input())

arr = list(map(int, input().split()))
arr.sort()
ans = 0

a = 1 if n % 2 == 0 else 2
for i in range(n//2+1) :
    sum_ = arr[i] + arr[n-i-a]

    if ans < sum_ :
        ans = sum_

print(ans)