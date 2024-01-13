import sys
from collections import deque
input = sys.stdin.readline

i = 1

while True :
    stack = deque()
    count = 0
    string = deque(input())
    string.pop()

    if string[0] == '-' :
        break
    while string :
        char = string.popleft()

        if char == '{' :
            stack.append(char)
                
        else :
            if stack :
                if stack[-1] == '{' :
                    stack.pop()
                else :
                    stack.append(char)
            else :
                stack.append(char)
        
    if stack :
        string2 = stack
        stack2 = []
        while string2 :
            char = string2.popleft()

            if stack2 :
                if stack2[-1] == char :
                    stack2.pop()
                    count += 1
                else :
                    stack2.pop()
                    count += 2
            else :
                stack2.append(char)

    print("{}. {}".format(i, count))
    i+=1