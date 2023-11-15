import sys
input = sys.stdin.readline

arr = [0 for _ in range(1000001)]
arr[0] = 1
arr[1] = 1

prime_num = []
for i in range(2, int(1000001**(1/2))) :
    if arr[i] == 0 :
        for j in range(i*2, 1000001, i) :
            arr[j] = 1

while True :
    num = int(input())

    if num == 0 :
        break
    is_break = False
    ans = "Goldbach's conjecture is wrong."
    for i in range(3, len(arr), 2) :
        if arr[i] == 0 and arr[num-i] == 0 :
            ans = "{} = {} + {}".format(num, i, num-i)
            break
    print(ans)