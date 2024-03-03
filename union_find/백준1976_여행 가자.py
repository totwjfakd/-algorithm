import sys

input = sys.stdin.readline

def find_root(x) :
    if parent[x] != x :
        parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b) :
    a = find_root(a)
    b = find_root(b)

    if a<b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())

map_ = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
seq = list(map(int, input().split()))
seq = list(map(lambda x:x-1, seq))

for i in range(n) :
    for j in range(i+1,n) :
        if map_[i][j] == 1 :
            union(i, j)
for i in range(m-1) :
    if find_root(seq[i]) != find_root(seq[i+1]) :
        print("NO")
        break
else :
    print("YES")