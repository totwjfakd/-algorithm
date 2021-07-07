n = int(input())

for i in range(n) :
    s = input()

    s = s.upper()
    '''
    size = len(s)
    for j in range(size//2) :
        if s[j] != s[-1-j] :
            print("#{} : No".format(i))
            break
    else :
        print("#{} : Yes".format(i))
    '''

    if s == s[::-1] :
        print("Yes")
    else :
        print("No")