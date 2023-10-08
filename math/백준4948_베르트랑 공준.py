arr = [0 for _ in range(250000)]


for i in range(2, 123457) :
    if arr[i] == 0 :
        for j in range(i*2, 250000, i) :
            arr[j] = 1

while True :
    n = int(input())
    if n == 0 :
        break
    count = 0

    for i in range(n+1, n*2+1) :
        if arr[i] == 0 :
            count += 1
    print(count)
