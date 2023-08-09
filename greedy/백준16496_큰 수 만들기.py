import functools
def compare(x, y) :
    if x+y > y+x :
        return -1
    elif x+y == y+x :
        return 0
    else :
        return 1
# return 음수 : 먼저 들어온 요소가 앞으로 정렬됨
# return 0 : 바뀌지 않음
# return 양수 : 나중에 들어온 요소가 앞으로 정렬됨(먼저들어온 요소보다 앞에 배치됨)
n = int(input())
arr = list(map(str, input().split()))
ans = sorted(arr, key=functools.cmp_to_key(compare))

print(int(''.join(ans)))