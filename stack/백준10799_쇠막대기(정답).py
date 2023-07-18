bar = input()

stack = []

ans = 0
for i in range(len(bar)) :
    if bar[i] == '(' :
        stack.append(i)
    else :
        left_idx = stack.pop()

        if i - left_idx == 1 : # 레이져 일때
            ans += len(stack)
        else :
            ans += 1


print(ans)
