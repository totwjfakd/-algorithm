from collections import deque

n = int(input())

arr = deque([i for i in range(1, n+1)])

c = 0
while len(arr) != 1 :
    c+=1
    if c == 2 :
        c = 0
        arr.popleft()
    else :
        arr.append(arr.popleft())
print(arr[0])
