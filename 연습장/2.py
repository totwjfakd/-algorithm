import sys
input = sys.stdin.readline

def find_root(x) :
    if parent[x] != x :
        parent[x] = find_root(parent[x])
    return parent[x]

def union(a,b) :
    a = find_root(a)
    b = find_root(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
know = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(m)]

if know[0] == 0 :
    print(m)
else :
    count = 0
    if know[0] == 1 :
        root = know[1]
    else :
        for i in range(1, know[0]) :
            union(know[i], know[i+1])
        root = parent[1]

    for i in range(m):
        if len(party[i]) > 2 :
            u = party[i][1:]
            for j in range(len(u)-1) :
                union(u[j], u[j+1])
        
    for p in party :
        if find_root(p[1]) != find_root(root) :
            count += 1
    print(count)




