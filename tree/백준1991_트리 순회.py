def dfs(start) :
    if start == '.' :
        return
    print(start, end = '')
    dfs(d[start][0])
    dfs(d[start][1])
def dfs2(start) :
    if start == '.' :
        return
    
    dfs2(d[start][0])
    print(start, end = '')
    dfs2(d[start][1])

def dfs3(start) :
    if start == '.' :
        return
    
    dfs3(d[start][0])
    dfs3(d[start][1])
    print(start, end = '')

num = int(input())

d = {}

for i in range(num) :
    start, left, right = input().split()
    d[start] = [left, right]
dfs('A')
print()
dfs2('A')
print()
dfs3('A')
print()