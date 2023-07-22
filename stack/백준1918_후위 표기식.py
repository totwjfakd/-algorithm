

s = input()

ans = ''

stack = []

for c in s :
    if c == '(' or c == ')' : #최우선순위
        if c == '(' :
            stack.append(c)
        else :
            while stack and stack[-1] != '(' : # 괄호 시작 지점까지 있는 연산자를 모두 ans에 추가해줘야함.
                ans+=stack.pop()
            stack.pop() # 괄호 시작 제거

    elif c == '*' or c == '/' : # 2순위
        while stack and (stack[-1] == '*' or stack[-1] == '/') : # * 혹은 / 일때, 먼저 스택에 들어와 있는 *, /를 ans에 추가해줘야함.
            ans += stack.pop()
        stack.append(c) # 새로 들어온 * 혹은 /는 스택에 추가.
    elif c == '+' or c == '-' : # 3순위
        while stack and stack[-1] != '(' : # 새로 들어온 +, -는 스택에 들어있던 +, -, *, / 보다 우선순위가 낮음. 때문에 스택에 들어있는 모든 연산자를 ans에 추가해줘야함.
            ans += stack.pop()
        stack.append(c)
    else : 
        ans += c
for c in stack[::-1] : # 스택에 남아있는 연산자 ans에 추가
    ans += c
print(ans)