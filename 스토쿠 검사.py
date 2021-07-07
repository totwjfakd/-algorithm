array = [list(map(int, input().split())) for _ in range(9)]

e = 0
s = 0
res = 1
array_s = [[[None]*3]*3]*9

for i in range(0, 7, 3) :
    for j in range(0, 7, 3) :        
        ch = [0] * 10
        for k in range(i, i+3, 1) :
            for q in range(j, j+3, 1) :
                ch[array[k][q]] = 1
        if sum(ch) != 9 :
            res = 0
for i in range(9) :    
    ch1 = [0] * 10
    ch2 = [0] * 10 
    for j in range(9) :
        ch1[array[i][j]] = 1
        ch2[array[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) != 9 :
        res = 0

if res == 1 :
    print("YES")
else :
    print("No")
