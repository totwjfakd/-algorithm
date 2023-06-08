import sys

t = int(input())

for i in range(t) :
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    k = 5
    while k <= n :
        cnt += n // k
        k *= 5

    print(cnt)