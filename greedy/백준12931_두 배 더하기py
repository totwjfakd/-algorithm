n = int(input())
B = list(map(int, input().split()))
count = 0
while sum(B) != 0 :
    for i in range(n) :
        if B[i] % 2 == 1 :
            B[i] -= 1
            break
    else :
        B = list(map(lambda x:x//2, B))
    count += 1
print(count)