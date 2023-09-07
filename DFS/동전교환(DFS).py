def dfs(deep, sum_) :
    global min__
    if sum_ == value :
        if min__ > deep :
            min__ = deep
        return
    elif sum_ > value or deep > min__:
        return
    for i in range(0, n) :
        dfs(deep+1, sum_ + coin[i])


n = int(input())
coin = list(map(int, input().split()))
value = int(input())
min__ = 999999
coin.sort(reverse=True)
print(coin)
dfs(0, 0)

print(min__)