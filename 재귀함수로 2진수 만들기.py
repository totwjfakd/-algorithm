
def makeBinaryNum(num) :
    global ans
    if num == 1 or num == 0 :
        return (ans+str(num))[::-1]
    ans+=str(num%2)
    return makeBinaryNum(num//2)

n = int(input())
ans = ''
print(makeBinaryNum(n))