import sys

def w(a, b, c) :
    global dp_arr
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)
    elif a < b and b < c :
        if dp_arr[a][b][c-1] != None :
            w1 = dp_arr[a][b][c-1]
        else :
            dp_arr[a][b][c-1] = w(a, b, c-1)    
            w1 = dp_arr[a][b][c-1]    
        if dp_arr[a][b-1][c-1] != None :
            w2 = dp_arr[a][b-1][c-1]
        else :
            dp_arr[a][b-1][c-1] = w(a, b-1, c-1)
            w2 = dp_arr[a][b-1][c-1]
        if dp_arr[a][b-1][c] != None:
            w3 = dp_arr[a][b-1][c]
        else :
            dp_arr[a][b-1][c] = w(a, b-1, c)
            w3 = dp_arr[a][b-1][c]
        return w1 + w2 - w3
    else :
        if dp_arr[a-1][b][c] != None :
            w1 = dp_arr[a-1][b][c]
        else :
            dp_arr[a-1][b][c] = w(a-1, b, c)
            w1 = dp_arr[a-1][b][c]
        if dp_arr[a-1][b-1][c] != None :
            w2 = dp_arr[a-1][b-1][c]
        else :
            dp_arr[a-1][b-1][c] = w(a-1, b-1, c)
            w2 = dp_arr[a-1][b-1][c]
        if dp_arr[a-1][b][c-1] != None :
            w3 = dp_arr[a-1][b][c-1]
        else :
            dp_arr[a-1][b][c-1] = w(a-1, b, c-1)
            w3 = dp_arr[a-1][b][c-1]
        if dp_arr[a-1][b-1][c-1] != None :
            w4 = dp_arr[a-1][b-1][c-1]
        else :
            dp_arr[a-1][b-1][c-1] = w(a-1, b-1, c-1)
            w4 = dp_arr[a-1][b-1][c-1]

        return w1 + w2 + w3 - w4


dp_arr = [[[None for i in range(21)] for j in range(21)] for k in range(21)]

while True :
    
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    
    if a == -1 and b == -1 and c == -1 :
        break

    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
    
