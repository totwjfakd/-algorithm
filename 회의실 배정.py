n = int(input())

array = []

for i in range(n) :
    array.append(list(map(int, input().split())))

array.sort(key=lambda x : x[1])

et = 0
cnt = 0
for s, e in tuple(array) :
    
    if s >= et :
        et = e
        cnt += 1
    
print(cnt)

