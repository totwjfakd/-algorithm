import sys
n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n+m) :
    fstr = sys.stdin.readline()
    fstr = fstr[:-1]
    arr1.append(fstr)
arr1.sort()

for i in range(n+m-1) :
    if arr1[i] == arr1[i+1] :
        arr2.append(arr1[i])

print(len(arr2))
for s in arr2 :
    print(s)
