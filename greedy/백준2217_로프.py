import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n) :
    arr.append(int(input()))
max_ = -1

arr.sort()

for i in range(n) :
    if max_ < arr[i] * (n-i) :
        max_ = arr[i] * (n-i)
print(max_)