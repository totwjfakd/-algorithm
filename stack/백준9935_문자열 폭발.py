s = input()
boom = input()

stack = []

for i in range(len(s)) :
    stack.append(s[i])
    if len(stack) >= len(boom) :
        if ''.join(stack[len(stack)-len(boom):]) == boom :
            for j in range(len(boom)) :
                stack.pop()
        

if len(stack) == 0 :
    print('FRULA')
else :
    print(''.join(stack))