from collections import deque
import sys

input = sys.stdin.readline

num = int(input().rstrip())

dq = deque()

for i in range(num) :
    s = input().rstrip().split()
    
    if s[0] == 'push_back' :
        dq.append(s[1])
    elif s[0] == 'push_front' :
        dq.appendleft(s[1])
    elif s[0] == 'pop_front' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq.popleft())
    elif s[0] == 'pop_back' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq.pop())
    elif s[0] == 'size' :
        print(len(dq))
    elif s[0] == 'empty' :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
    elif s[0] == 'front' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq[0])
    elif s[0] == 'back' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq[-1])
