n = int(input())

body = []
for i in range(n) :
    body.append(list(map(int, input().split())))

body.sort(key=lambda x:x[0], reverse=True)

count = 1
max_weight = body[0][1]

for i in range(1, n) :
    if max_weight < body[i][1] :
        max_weight = body[i][1]
        count += 1
print(count)