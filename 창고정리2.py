def re_batch() :
    min_idx = -1
    min_value = 999
    max_idx = -1
    max_value = -999

    for j in range(n) :
        if arr[j] < min_value :
            min_idx = j
            min_value = arr[j]
        if arr[j] > max_value :
            max_idx = j
            max_value = arr[j]
    arr[max_idx] -= 1
    arr[min_idx] += 1

n = int(input())

arr = list(map(int, input().split()))

r = int(input())

for i in range(r) :
    re_batch()
print(max(arr) - min(arr))