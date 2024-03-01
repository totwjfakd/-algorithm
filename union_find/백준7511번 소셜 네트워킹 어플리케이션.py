import sys

def find_root(parent, x) :
    if parent[x] != x :
        return find_root(parent, parent[x])
    return x

def union(parent, a, b) :
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

input = sys.stdin.readline

testcase = int(input())


for i in range(testcase) :
    n = int(input())
    parent = [j for j in range(n)]

    friend_relationship_num = int(input())

    for j in range(friend_relationship_num) :
        s, e = map(int, input().split())
        union(parent, s, e)
    
    search_num = int(input())
    ans = []
    for j in range(search_num) :
        start, find = map(int, input().split())
        if find_root(parent, start) == find_root(parent, find) :
            ans.append(1)
        else :
            ans.append(0)
    print("Scenario {}:".format(i+1))
    for a in ans :
        print(a)
    print()
