n = int(input())

books = {}
for i in range(n) :
    name = input()

    if not name in books :
        books[name] = 1
    else :
        books[name] += 1
maxnum = -9999999
ans = ''
for k, v in books.items() :
    if maxnum < v :
        ans = k
        maxnum = v
    elif maxnum == v :
        if ans < k :
            continue
        else :
            ans = k


print(ans)