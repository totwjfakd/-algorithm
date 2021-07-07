num1 = int(input())
list1 = list(map(int, input().split()))

num2 = int(input())
list2 = list(map(int, input().split()))

p1 = 0
p2 = 0
list_res = []
for _ in range(num1+num2) :
    if list1[p1] < list2[p2] :
        list_res.append(list1[p1])
        p1 +=1
        if p1 == num1 :
            break
    else :
        list_res.append(list2[p2])
        p2 += 1
        if p2 == num2 :
            break

if p1 == num1 :
    list_res += list2[p2:]
elif p2 == num2 :
    list_res += list1[p1:]
print(list_res)