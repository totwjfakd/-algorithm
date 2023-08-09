s = input()

alphabet = {}

for c in s :
    if c in alphabet :
        alphabet[c] += 1
    else :
        alphabet[c] = 1
ans = ''
cnt = 0
center_char = ''
for k, v in alphabet.items() :
    if v % 2 != 0 :
        cnt += 1
        center_char = k
        if cnt >= 2 :
            print('I\'m Sorry Hansoo')
            exit()
for k, v in sorted(alphabet.items()) :
    ans += k * (v // 2)
print(ans + center_char + ans[::-1])