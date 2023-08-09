from collections import deque

n = int(input())

arr = list(map(int, input().split()))

dq = deque()

for i in range(n) :
    dq.append([i+1, arr[i]])


ans = []
while len(dq) != 1 :
    
    pop_balloon = list(dq.popleft())

    move_point = pop_balloon[1]
    ans.append(str(pop_balloon[0]))
    
    if move_point < 0 :
        for i in range(0, -move_point) :
            dq.appendleft(dq.pop())
    else :
        for i in range(0, move_point-1) :
            dq.append(dq.popleft())

ans.append(str(dq.pop()[0]))

print(' '.join(ans))