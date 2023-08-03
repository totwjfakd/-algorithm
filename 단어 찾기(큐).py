from collections import deque

n = int(input())

dq = deque()

for i in range(n) :
    dq.append(input())

for i in range(n-1) :
    s = input()

    while dq[0] != s :
        dq.append(dq.popleft())
    dq.popleft()
print(dq[0])