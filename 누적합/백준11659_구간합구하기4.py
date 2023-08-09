import sys

n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(1, n) :
    arr[i] += arr[i-1]


for k in range(m) :
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1 :
        print(arr[j-1])
    else :
        print(arr[j-1] - arr[i-2])
