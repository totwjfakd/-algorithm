from collections import deque

n = int(input())
stack = deque()

arr = deque(list(map(int, input().split())))

ans = 'Nice'
c = 1
while True :
    if len(stack) >= 1 :
        if stack[-1] == c :
            stack.pop()
            c+=1
        else :
            if len(arr) >= 1 :
                stack.append(arr.popleft())
            else :
                ans = 'Sad'
                break
    else :
        if len(arr) >= 1 :
            stack.append(arr.popleft())
        else :
            if len(stack) == 0 :
                break
print(ans)



