from collections import deque

n, k = map(int, input().split())

count = 0
arr = deque([i for i in range(1, n+1)])

while len(arr) != 1 :


    if len(arr) < k :
        arr.pop()

    else :
        for i in range(k) :
            if i == 0 :
                arr.append(arr.popleft())
            else :
                arr.popleft()
            

print(arr[0])