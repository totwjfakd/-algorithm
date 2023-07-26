from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))
que = deque()
for i in range(n) :
    que.append([arr[i], i])

count = 0
while True :
    if que[0] == max(que, key = lambda x:x[0]) :
        count += 1
        poplist = que.popleft()
        if poplist[1] == m :
            print(count)
            break
    else :
        que.append(que.popleft())
        