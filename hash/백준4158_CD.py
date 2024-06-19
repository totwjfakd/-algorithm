import sys

input = sys.stdin.readline
while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    dict_ = {}

    for i in range(n) :
        dict_[int(input())] = 1
    count = 0 
    for i in range(m) :
        num = int(input())
        if num in dict_ : 
            count += 1

    print(count)