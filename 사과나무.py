num = int(input())

array = [list(map(int, input().split())) for _ in range(num)]

res = 0
over_h = 0
s = e = num//2
e += 1
index = 0
for j in range(num) :
    
    for i in range(s, e, 1) :
        res += array[j][i]

    if s == 0 :
        over_h = 1

    if over_h == 0 :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1
print(res)