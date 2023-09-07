import sys

input = sys.stdin.readline

def dfs(money_sum, s) :
    global count
    if money_sum > T :
        return
    elif money_sum == T :
        count += 1
        return
    for i in range(s, k) :
        if coin_use[i] + 1 <= arr[i][1] :
            coin_use[i] += 1
            dfs(money_sum + arr[i][0], i)
            coin_use[i] -= 1

T = int(input())
k = int(input())
arr = []

for i in range(k) :
    coin_value, coin_num = map(int, input().split())
    arr.append([coin_value, coin_num])

count = 0
coin_use = [0 for _ in range(k)]
dfs(0, 0)
print(count)