n = int(input())

num = list(map(int,input().split()))
num2 = list(set(num))
num2.sort()


num_dict = {}
for i in range(len(num2)) :
    num_dict[num2[i]] = i

answer=[]
for i in num :
    answer.append(str(num_dict[i]))

a = ' '.join(c for c in answer)
print(a)
