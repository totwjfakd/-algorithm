N, M = map(int, input().split())
num_list = list(map(int, input().split()))

lt = 0
rt = N-1

num_list.sort()
num = 0
while lt<=rt :
    lt_rt = num_list[lt]+num_list[rt]
    if lt_rt <= M :
        lt+=1
        rt-=1
    else :
        rt-=1
    num += 1

print(num)