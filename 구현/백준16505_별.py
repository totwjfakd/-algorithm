import re

def func(num) :
    if num == 0 :
        return '*'
    stars = func(num-1)
    L = []

    
    for s in stars :
        L.append(s*2)
    i = 2**(num-1) 

    for s in stars :

        L.append(re.sub(r"\s+$", "", s) + ' '*i)
        i+=1


    return L
n = int(input())

for str_ in func(n) :
    print(re.sub(r"\s+$", "", str_))