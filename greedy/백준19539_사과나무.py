num = int(input())
arr = list(map(int, input().split()))
count = 0
if sum(arr) % 3 != 0:
    print("NO")
else :
    for i in range(num) :
        count += arr[i]//2
    if count >= sum(arr) // 3:
        print("YES")
    else :
        print("NO")