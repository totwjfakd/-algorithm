from collections import deque

num = int(input())

for _ in range(num) :
    command = input()

    n = int(input().rstrip())
    s = input()
    if n == 0 :
        que = deque()
    else :
        que = deque(map(int, s[1:-1].split(',')))
    try :
        reverseTF = False
        for c in command :
            if c == 'D' and not reverseTF:
                que.popleft()
            elif c == 'D' and reverseTF :
                que.pop()
            elif c == 'R' :
                reverseTF = not reverseTF

        if reverseTF :
            que = list(map(str, que))[::-1]
            ans = ','.join(que)
            print('[{}]'.format(ans))
        else :
            que = list(map(str, que))
            ans = ','.join(que)
            print('[{}]'.format(ans))

    except :
        print('error')
