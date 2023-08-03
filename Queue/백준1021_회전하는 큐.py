from collections import deque
import copy

n, m = map(int, input().split())

arr = deque(map(int, input().split()))

dq = deque(i for i in range(1, n+1))

ans = 0
while arr :
    if arr[0] == dq[0] :
        arr.popleft()
        dq.popleft()
    else :
        dq_1 = copy.deepcopy(dq)
        dq_2 = copy.deepcopy(dq)
        
        c1 = 0
        c2 = 0

        while dq_1[0] != arr[0] :
            dq_1.append(dq_1.popleft())
            c1 += 1
        dq_1.popleft()
        while dq_2[0] != arr[0] :
            dq_2.appendleft(dq_2.pop())
            c2 += 1
        dq_2.popleft()
        arr.popleft()
        if c1 <= c2 :
            dq = copy.deepcopy(dq_1)
            ans += c1
        else :
            dq = copy.deepcopy(dq_2)
            ans += c2
print(ans)