import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n) :
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])

for i in range(n) :
    if i == 0:
        start, end = arr[i][0], arr[i][1]
        ans = end-start
    new_start, new_end = arr[i][0], arr[i][1]
    if end >= new_start :
        if end >= new_end :
            continue
        ans += new_end - end
        end = new_end
        
    else :
        start = new_start
        end = new_end
        ans += end-start
print(ans)