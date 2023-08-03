def cantorian(s) :
    length = len(s)
    if length == 1 :
        return '-'
    space = ' '*(length//3)
    newS = '-'*(length//3) + space + '-'*(length//3)
    return cantorian(newS.split()[0]) + space + cantorian(newS.split()[1])

while True :
    try :
        n = int(input())
        
        ans = cantorian(pow(3,n)*'-')

        print(ans)
    except :
        break