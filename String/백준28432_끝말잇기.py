
num = int(input())
arr = []
for i in range(num) :
    arr.append(input())
arr2 = []
num2 = int(input())
for i in range(num2) :
    arr2.append(input())

if num == 1 :
    print(arr2[0])
else :
    for i in range(num) :
        if arr[i] == '?' :
            if i == 0 :
                for j in range(num2) :
                    if arr[i+1][0] == arr2[j][-1] :
                        if not arr2[j] in arr :
                            print(arr2[j])
                            exit()
            elif i == num-1 :
                for j in range(num2) :
                    if arr[i-1][-1] == arr2[j][0] :
                        if not arr2[j] in arr :
                            print(arr2[j])
                            exit()
            else :
                for j in range(num2) :
                    if arr[i-1][-1] == arr2[j][0] and arr[i+1][0] == arr2[j][-1] :
                        if not arr2[j] in arr :
                            print(arr2[j])
                            exit()