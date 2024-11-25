n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.append(arr[0])
s = 0
for i in range(n):
    s+=arr[i][0]*arr[i+1][1] - arr[i+1][0]*arr[i][1]
print(round(abs(s/2), 1))


# 신발끈 공식 사용