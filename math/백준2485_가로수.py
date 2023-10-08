import sys, math
input = sys.stdin.readline


n = int(input())
last_num = int(input())

arr = []
for i in range(n-1) :
    a = int(input())
    arr.append( a- last_num)
    last_num = a
num = arr[0]

for i in range(1, n-1) :
    gcd_num = math.gcd(num, arr[i])
    num = gcd_num

ans = 0

for number in arr :
    ans += number // gcd_num - 1

print(ans)