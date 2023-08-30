
n = int(input())

count = 0

for i in range(n) :
    stack = []
    s = input()

    for c in s :
        if len(stack) == 0 :
            stack.append(c)
        elif stack[-1] != c :
            stack.append(c)
        elif c == stack[-1] :
            stack.pop()
    if len(stack) == 0 :
        count += 1

print(count)