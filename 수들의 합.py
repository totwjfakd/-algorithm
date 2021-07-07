n, m = map(int, input().split())
array = list(map(int, input().split()))

'''첫번째 방법
# 8 3
# 1 2 1 3 1 1 1 2
play = 0
res = 0
for i in range(n-1) :
    lt = i
    total = array[i]
    if total == m :
        res+=1
        continue
    for j in range(lt+1, n, 1) :
        rt = j
        total += array[j]
        play += 1
        if total == m :
            res += 1
            break

print(res, play)

'''
tot = array[0]
res = 0
lt = 0
rt = 1
while True :

    if tot < m :
        if rt < n :
            tot += array[rt]
            rt += 1 
        else :
            break
    elif tot == m :
        res += 1
        tot -= array[lt]
        lt += 1
    elif tot > m :
        tot -= array[lt]
        lt += 1
print(res)