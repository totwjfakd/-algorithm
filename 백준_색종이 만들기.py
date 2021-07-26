def slice(arr, n) :
    s_array = []

    for i in range(4) :
        t_array = []
        for j in range(0, n//2) :
            if i == 0 :
                t_array.append(arr[j][:n//2])
            elif i == 1 :
                t_array.append(arr[j][n//2:])
            elif i == 2 :
                t_array.append(arr[n//2+j][:n//2])
            elif i == 3 :
                t_array.append(arr[n//2+j][n//2:])
        s_array.append(t_array)
    return s_array
def square(arr) :
    s = 0
    n = len(arr)
    global w, b
    
    for l in arr :
        s += sum(l)

    if s == 0 :
        w += 1
        return 0
    elif s == n**2 :
        b += 1
        return 0
    else :
        new_array = slice(arr, n)
        square(new_array[0])
        square(new_array[1])
        square(new_array[2])
        square(new_array[3])

w = 0
b = 0
n = int(input())
array = []

for i in range(n) :
    array.append(list(map(int, input().split())))


square(array)
print(w)
print(b)
