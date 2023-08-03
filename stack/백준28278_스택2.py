from collections import deque
import sys
stack = deque()

n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    num = sys.stdin.readline().rstrip().split()


    if num[0] == '2' :
        if len(stack) != 0 :
            print(stack.pop())
        else :
            print(-1)
    elif num[0] == '3' :
        print(len(stack))
    elif num[0] == '4' :
        if len(stack) != 0 :
            print(0)
        else :
            print(1)
    elif num[0] =='5' :
        if len(stack) != 0 :
            print(stack[-1])
        else :
            print(-1)
    elif num[0] == '1' :
        stack.append(int(num[1]))
