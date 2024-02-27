import sys

def dfs(depth, choice, visit, start) :
    global count
    if depth == N+1 :
        return
    if depth >= 2 :
        if L <= sum(choice) <= R and max(choice) - min(choice) >= X:
            count += 1
    for i in range(start, N) :
        if not visit[i] :
            visit[i] = True
            dfs(depth+1, choice + [A[i]], visit, i)
            visit[i] = False
count = 0

N, L, R, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N) :
    visit = [False for _ in range(N)]

    visit[i] = True
    dfs(1,[A[i]], visit, i)
print(count)