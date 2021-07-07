num = int(input())

array = [list(map(int, input().split())) for _ in range(num)]

num_command = int(input())
command = [list(map(int, input().split())) for _ in range(num_command)]


for i in range(num_command) :
    col = command[i][0]-1
    direction = command[i][1]
    count = command[i][2]

    if direction == 0 :
        for _ in range(count) :
            ch = array[col].pop(0)
            array[col].append(ch)
    else :
        for _ in range(count) :
            ch = array[col].pop()
            array[col].insert(0, ch)

s = 0
e = num
res = 0
over_h = 0
for i in range(num) :
    for j in range(s, e) :
        res += array[i][j]
    if over_h == 0 :
            s += 1
            e -= 1
    else :
        s -= 1
        e += 1
    if s+1 == e :
        over_h = 1

print(res)

