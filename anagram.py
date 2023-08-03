s1 = input()
s2 = input()

s1dict = {}
s2dict = {}

for c in s1 :
    if c not in s1dict :
        s1dict[c] = 1
    else :
        s1dict[c] += 1

for c in s2 :
    if c not in s2dict :
        s2dict[c] = 1
    else :
        s2dict[c] += 1

ans = 'YES'
for k, v in s1dict.items() :
    if k in s2dict :
        if s2dict[k] == v :
            continue
        else :
            ans = 'NO'
            break
    else :
        ans = 'NO'
        break
print(ans)