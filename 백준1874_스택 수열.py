import sys

n = int(input())
stack = []
ans = []
c = 0
for i in range(1,n+1) :
    stack_num = int(sys.stdin.readline().rstrip())
    while c < stack_num :
        stack.append(c+1)
        ans.append("+")
        c += 1
    if stack.pop() == stack_num :
        ans.append("-")
    else :
        print("NO")
        sys.exit(0)

print('\n'.join(ans))