def dfs(depth, Alphabet) :
    global count
    if depth == input_lenth :
        print(Alphabet)
        count += 1
        return
    for i in range(1, 3) :
        #print(password[depth:depth+i])
        if int(password[depth:depth+i]) < 27 and depth+i <= input_lenth :
            if int(password[depth:depth+i]) == 0 :
                return
            dfs(depth+i, Alphabet+chr(int(password[depth:depth+i])+64))

password = input()
input_lenth = len(password)
count = 0
dfs(0, '')
print(count)
