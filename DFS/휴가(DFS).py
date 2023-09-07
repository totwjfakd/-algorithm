import sys
input = sys.stdin.readline

def dfs(days, money) :
    global max_money
    if days == n + 1:
        if max_money < money :
            max_money = money
    
    if days > n :
        return

    dfs(days+arr[days][0], money+arr[days][1])
    dfs(days+1, money)

n = int(input())

arr = [None]

for i in range(n) :
    arr.append(list(map(int, input().split())))
max_money = 0

dfs(1, 0)
print(max_money)