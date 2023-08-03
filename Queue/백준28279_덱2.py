from collections import deque
import sys

n = int(sys.stdin.readline().strip())

dq = deque()
for i in range(n) :
    num = sys.stdin.readline().strip().split()
    if num[0] == '1' :
        dq.appendleft(int(num[1]))
    elif num[0] == '2' :
        dq.append(int(num[1]))
    elif num[0] == '3' :
        if len(dq) != 0 :
            print(dq.popleft())
        else :
            print(-1)
    
    elif num[0] == '4' :
        if len(dq) != 0 :
            print(dq.pop())
        else :
            print(-1)
    elif num[0] == '5' :
        print(len(dq))
    elif num[0] == '6' :

        if len(dq) != 0 :
            print(0)
        else :
            print(1)
    elif num[0] == '7' :
        if len(dq) != 0 :
            print(dq[0])
        else :
            print(-1)
    elif num[0] == '8' :
        if len(dq) != 0 :
            print(dq[-1])
        else :
            print(-1)