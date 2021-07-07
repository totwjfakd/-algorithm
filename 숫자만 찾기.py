s = input()
res = 0
for x in s :

    if x.isdecimal() : # 문자열이 0~9까지의 숫자인지 확인
       res = res * 10 + int(x)

count = 0
for i in range(1, res+1) :
    if res % i == 0 :
        count += 1
        print(i)

print(res)
print(count)