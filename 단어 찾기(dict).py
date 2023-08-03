
n = int(input())

d = {}
for i in range(n) :
    d[input()] = 1

for i in range(n-1) :
    d[input()] = 0

d2 = {v : k for k, v in d.items()}

print(d2[1])