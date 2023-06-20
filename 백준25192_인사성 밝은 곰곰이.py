import sys

num = int(input())
chat_count = {}
ans = 0

for i in range(num) :
    s = sys.stdin.readline().rstrip()
    if s == 'ENTER' :
        chat_count = {}
    else :
        if chat_count.get(s) == 1:
            continue
        else :
            ans += 1
            chat_count[s] = 1

print(ans)