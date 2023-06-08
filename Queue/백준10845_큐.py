from collections import deque
import sys
dq = deque([])

n = int(input())

for i in range(n) :
    input_str = sys.stdin.readline().rstrip().split()

    if input_str[0] == 'push' :
        dq.append(input_str[1])
    if input_str[0] == 'front' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq[0])
    if input_str[0] == 'back' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq[-1])
    if input_str[0] == 'size' :
        print(len(dq))
    if input_str[0] == 'empty' :
        if len(dq) == 0 :
            print('1')
        else :
            print('0')
    if input_str[0] == 'pop' :
        if len(dq) == 0 :
            print('-1')
        else :
            print(dq.popleft())
        