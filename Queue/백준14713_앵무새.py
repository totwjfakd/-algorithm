from collections import deque

n = int(input())

sentences = []

for i in range(n) :
    sentences.append(deque(input().split()))

cseteram_sentence = deque(input().split())


while cseteram_sentence :
    now = cseteram_sentence.popleft()

    ans = False

    for i in range(len(sentences)) :
        if len(sentences[i]) > 0 :
            if now == sentences[i][0] :
                sentences[i].popleft()
                ans = True
                break

    if not ans :
        print('Impossible')
        exit()
for sentence in sentences :
    if len(sentence) != 0 :
        print('Impossible')
        exit()
print('Possible')