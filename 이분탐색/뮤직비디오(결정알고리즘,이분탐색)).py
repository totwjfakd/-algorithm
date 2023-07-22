def count(capacity) :
    cnt = 1
    sum = 0
    for x in sing :
        if sum + x > capacity :
            cnt += 1
            sum = x
        else :
            sum += x
    return cnt

n, m = map(int, input().split())

sing = list(map(int, input().split()))
maxx = max(sing)
lt = 1
rt = sum(sing)
res = 0
while lt < rt :
    center = (lt+rt)//2
    if center>=maxx and count(center) <= m :
        rt = center - 1
        res = center
    else :
        lt = center + 1
if max(sing) > res :
    res = max(sing)
print (res)
    