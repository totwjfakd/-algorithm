import sys

def find_root(x) :
    if parent[x] != x :
        parent[x] = find_root(parent[x])
    return parent[x]
def union(a, b) :
    a = find_root(a)
    b = find_root(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

input = sys.stdin.readline

n, case = map(int, input().split())

parent = [i for i in range(n)]
for i in range(case) :
    a, b = map(int, input().split())
    union(a-1, b-1)
g = list(map(lambda x:x-1, list(map(int, input().split()))))

count = 0
for i in range(n-1) :
    if find_root(g[i]) != find_root(g[i+1]) :
        count += 1
print(count)
