from collections import deque

n, k = map(int, input().split())

que = deque()

for i in range(1, n+1) :
    que.append(str(i))
ans = []
c = 1
while len(que) > 1 :
    if c != k :
        que.append(que.popleft())
        c += 1
    else :
        c = 1
        ans.append(que.popleft())
ans.append(que.pop())

d = ', '.join(ans)
print('<{}>'.format(d))