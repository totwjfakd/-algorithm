import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b) :
    a = find(a)
    b = find(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m) :
    t, a, b = map(int, input().split())

    if t == 0 :
        union(a, b)
    else :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")
print(parent)