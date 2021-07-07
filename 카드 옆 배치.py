card_list = list(range(1, 21, 1))

for i in range(10) :
    n1, n2 = map(int, input().split())

    for j in range(((n2-n1)+1)//2) :
        card_list[n1+j-1], card_list[n2-j-1] = card_list[n2-j-1], card_list[n1+j-1]
print(len(card_list))
for i in card_list :
    print(i, end = " ")