n = int(input())
ab = []
minNum = 99999
minIndex = -1

for i in range(n) :
    ab.append(list(map(int, input().split())))
    if ab[i][0] > ab[i][1] :
        continue
    else :
        if minNum > ab[i][1] :
            minNum = ab[i][1]
            minIndex = i
        
    
if minIndex != -1 :
    print(minNum)
else :
    print(minIndex)
