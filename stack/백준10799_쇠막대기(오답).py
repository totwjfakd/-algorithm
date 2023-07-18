bar = input()

stack = []

r_idx = []
b_idx = []

for i in range(len(bar)) :
    if bar[i] == '(' :
        stack.append(i)
    else :
        left_idx = stack.pop()

        if i - left_idx == 1 :
            r_idx.append([left_idx, i]) # 레이져 시작, 끝 인덱스
        else :
            b_idx.append([left_idx, i]) # 쇠박대기 시작, 끝 인덱스

ans = 0
for b in b_idx :
    count = 0
    for r in r_idx :
        if b[0] < r[0] and b[1] > r[1] : # 하나의 쇠 막대기 안에 몇개의 레이져가 있는지 판단
            count += 1
    ans += count + 1 # 잘린 쇠막대기 수는 레이져 수 + 1

print(ans)

