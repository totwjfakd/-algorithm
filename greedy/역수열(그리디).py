def create_arr(ans_arr, num, idx) :
    none_counter = 0
    if none_counter == num :
        for j in range(0,n,) :
            if ans_arr[j] == None :
                ans_arr[j] = idx
                return 0

    for j in range(n) :
        if ans_arr[j] == None :
            none_counter += 1

        if none_counter == num :
            for k in range(j+1,n,1) :
                if ans_arr[k] == None :
                    ans_arr[k] = idx
                    break
            break


n = int(input())

arr = list(map(int, input().split()))

ans = [None for _ in range(n)]

for i in range(n) :
    create_arr(ans, arr[i], i+1)

print(ans)