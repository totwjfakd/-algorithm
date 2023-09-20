
num = int(input())
m = int(input())

if m != 0:
   del_button = list(map(int, input().split()))
else :
    del_button = []


min_count = abs(int(num)-100)

for number in range(1000001) :
    make_num = str(number)

    for i in range(len(make_num)) :
        if int(make_num[i]) in del_button :
            break

        if i == len(make_num)-1 :
            
            if min_count > len(make_num) + abs(int(make_num)-int(num)) :
                min_count =  len(make_num) + abs(int(make_num)-int(num))

print(min_count)

# https://seongonion.tistory.com/99
# 이건 다시 풀어보자