def dfs(num, sumNum) :
    if num > len(arr)-1 :
        if sumNum == arr_sum-sumNum :
            print("YES")
            exit()

        return
    if sumNum > arr_sum // 2 :
        return    
    dfs(num+1, sumNum+arr[num])
    dfs(num+1, sumNum)

n = int(input())

arr = list(map(int, input().split()))
arr_sum = sum(arr)

dfs(0, 0)
print("NO")