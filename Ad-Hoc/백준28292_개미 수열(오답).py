n = int(input())

arr = ['1']
for i in range(n-1) :
    for s in arr :
        count = 0
        new_arr = ''
        for j in range(len(s)) :
            if j == 0 :
                first_char = s[j]
                count += 1
            else :
                if s[j] != first_char :
                    new_arr += first_char + str(count)
                    first_char = s[j]
                    count = 1
                else :
                    count += 1

        new_arr += first_char + str(count)
    arr.append(new_arr)
max_num = -1
for c in arr[n-1] :
    if int(c) > max_num :
        max_num = int(c)
print(max_num)