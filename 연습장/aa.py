def combi(depth, make_arr) :
    if depth == 7 :
        sum_ = 0
        for i in make_arr :
            sum_ += arr[i]
        if sum_ == 100 :
            for i in make_arr :
                print(arr[i])
            exit()
    for j in range(9) :
        if not j in make_arr :
            make_arr.append(j)
            combi(depth+1, make_arr)
            make_arr.pop()

arr = []
for i in range(9) :
    arr.append(int(input()))
arr.sort()

combi(0, [])