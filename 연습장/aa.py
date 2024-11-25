
n = int(input())


for i in range(n) :
    string = input()
    lt = 0
    rt = len(string)-1

    continue_flag = False
    del_count = 0
    flag = False
    while lt <= rt:

        if string[lt] != string[rt]:
            if lt+1 <= rt and string[lt+1:rt+1] == string[lt+1:rt+1][::-1]:
                del_count += 1
                lt += 1
            elif lt <= rt-1 and string[lt:rt] == string[lt:rt][::-1]:
                del_count += 1
                rt -= 1
            else :
                flag = True
        if flag or del_count >= 2:
            continue_flag = True
            print(2)
            break
        lt+=1
        rt-=1
    if not continue_flag and del_count == 1 :
        print(1)
    elif not continue_flag and del_count == 0:
        print(0)

    

