

a = int(input())

for i in range(a, 0, -1) : 
    num_len = len(str(i))
    num_str = str(i)
    flag = False
    for j in range(num_len) :
        if num_str[j] == '4' or num_str[j] == '7' :
            continue
        else :
            flag = True
            break
    if flag :
        continue
    else :
        print(num_str)
        break