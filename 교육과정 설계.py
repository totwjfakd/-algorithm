cmd = input()
num = int(input())

for i in range(num) :
    s = input()
    cnt = 0
    arr =[]
    for c in s :
        if c == cmd[cnt] :
            arr.append(c)
            cnt += 1
            if cnt >= len(cmd) :
                cnt-=1
                break
    print(arr)
    ans = ''.join(arr)
    if cmd == ans :
        print("YES")
    else :
        print("NO")