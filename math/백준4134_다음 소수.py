import sys

input = sys.stdin.readline

n = int(input())

for i in range(n) :
    number = int(input())
    if number == 0 or number == 1 :
        print(2)
    else :
        for j in range(number, number*2) :

            prime = True
            tmp = int(j**(1/2))+1
            for k in range(2, tmp) :
                if j%k == 0 :
                    prime = False
                    break
            if prime :
                print(j)
                break

