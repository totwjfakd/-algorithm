import re
num = input()
plus_minus = []
for c in num :
    if not c.isdigit() :
        plus_minus.append(c)
num = re.split('[+|-]', num)

plus_minus_index = 0

minus = []
plus = []
minus_bool = False

for i in range(len(num)) :
    if i == 0 :
        plus.append(int(num[i]))
    else :
        if plus_minus[plus_minus_index] == '+' and not minus_bool:
            plus.append(int(num[i]))
            plus_minus_index+=1
        elif plus_minus[plus_minus_index] == '+' :
            if minus_bool :
                minus.append(int(num[i]))
                plus_minus_index+=1
        elif plus_minus[plus_minus_index] == '-' :
            minus.append(int(num[i]))
            minus_bool = True
            plus_minus_index+=1

print(sum(plus)-sum(minus))