num = int(input())

array = [1] * 4000001
array[0] = 0
array[1] = 0

for i in range(2, 4000001) :
    if array[i] == 0 :
        continue
    for j in range(i, 4000001, i) :
        if i==j :
            continue
        array[j] = 0 
answer = 0
#print(array[:10])
for i in range(2, num+1, 1) :
    s = 0
    if array[i] != 1 :
        continue
    for j in range(i, num+1, 1) :
        if array[j] == 1 :
            s += j
            
            
        if s == num :
            answer += 1
            break
        elif s > num :
            break

print(answer)
