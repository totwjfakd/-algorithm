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

lt = 1
rt = sum(sing)
res = 0
while lt < rt :
    center = (lt+rt)//2
    if count(center) <= m :
        rt = center - 1
        res = center
    else :
        lt = center + 1

print (res)
    