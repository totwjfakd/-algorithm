n, m = map(int, input().split())

g = [[0 for _ in range(n+1)] for _ in range(n+1)]

print(g)

for i in range(m) :
    c, r, v = map(int, input().split())

    g[c][r] = v

for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(g[i][j], end = ' ')
    print()