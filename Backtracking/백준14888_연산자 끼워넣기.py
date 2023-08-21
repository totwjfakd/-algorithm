
def dfs(deep, oper_arr, v) :
    global min_, max_

    if deep == n-1 :
        if v > max_ :
            max_ = v
        if v < min_ :
            min_ = v
        return

    for i in range(len(oper_arr)) :
        new_arr = oper_arr[:i]+oper_arr[i+1:]
        if oper_arr[i] == '+' :
            dfs(deep+1, new_arr, v+num_arr[deep+1])
        elif oper_arr[i] == '-' :
            dfs(deep+1, new_arr, v-num_arr[deep+1])
        elif oper_arr[i] == '*' :
            dfs(deep+1, new_arr, v*num_arr[deep+1])
        elif oper_arr[i] == '//' :
            dfs(deep+1, new_arr, int(v/num_arr[deep+1]))


n = int(input())
num_arr = list(map(int, input().split()))
arr = list(map(int, input().split()))

operator_arr = []

for i in range(4) :
    for j in range(arr[i]) :
        if i == 0 :
            operator_arr.append('+')
        elif i == 1 :
            operator_arr.append('-')
        elif i == 2 :
            operator_arr.append('*')
        else :
            operator_arr.append('//')

min_ = 1000000001
max_ = -1000000001

dfs(0, operator_arr, num_arr[0])
print(max_)
print(min_)