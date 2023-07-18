s, n = tuple(input().split())

n = int(n)

arr = []
count = 0

for i in range(len(s)) :
    if i == 0 :
        arr.append(s[i])
    else :
        if count < n :
            for j in range(len(arr)-1, -1, -1) :
                if int(arr[j]) < int(s[i]) :
                    arr.pop()
                    count += 1
                    if count >= n :
                        break
                else :
                    break
            arr.append(s[i])
        else :
            arr.append(s[i])
sn = n - count

for i in range(sn) :
    arr.pop()

print(''.join(arr))