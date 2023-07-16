n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))


lp = 0
rp = n-1
ans = 0
while lp <= rp :
    sumOfTwoPeople = arr[lp] + arr[rp]
    if sumOfTwoPeople <= m :
        arr[lp] = -1
        arr[rp] = -1
        rp -= 1
        lp += 1
        ans += 1
    else :
        rp -= 1
    
for v in arr :
    if v != -1 :
        ans += 1 
print(ans)