# def pow_(n) :
#     if n == 1 :
#         return a
#     x = pow_(n//2)
#     if n % 2 == 0 :
#         return x * x
#     else :
#         return x * x * a

def pow_(n) :
    global a
    res = 1
    while n :
        if n % 2 == 1 :
            res *= a
        a *= a
        a %= c
        res %= c
        n //= 2
    return res

a, b, c = map(int, input().split())

print(pow_(b))

