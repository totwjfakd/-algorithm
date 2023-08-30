n = int(input())

arr1 = list(map(int, input().split()))
num_dict = {}
for num in arr1 :
    if not num in num_dict :
        num_dict[num] = 1
    else :
        num_dict[num] += 1
ans = []
n2 = int(input())
arr2 = list(map(int, input().split()))

for num in arr2 :
    if not num in num_dict :
        ans.append('0')
    else :
        ans.append(str(num_dict[num]))

print(' '.join(ans))