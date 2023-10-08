from collections import deque
import sys

input = sys.stdin.readline

def bfs() :
    queue = deque()
    queue.append(1)
    visit[1] = 1
    c = 0
    while queue :
        for_len = len(queue)
        for _ in range(for_len) : # 깊이 측정을 위한 for문
            now = queue.popleft()
            if now == 100 :
                return c
            for i in range(1, 7) :
                next = now + i
                if next > 100 :
                    continue
                if visit[next] == 0 : # 한번 지났던 길은 다시 queue에 넣지 않음
                    if next in snakes :
                        queue.append(snakes[next])
                    elif next in ladders :
                        queue.append(ladders[next])
                    else :
                        queue.append(next)
                    visit[next] = 1
        c+=1

l, s = map(int, input().split())

snakes = {}
ladders = {}
visit = [0 for _ in range(101)]
for i in range(l) :
    x, y = map(int, input().split())
    ladders[x] = y

for i in range(s) : 
    x, y = map(int, input().split())
    snakes[x] = y
print(bfs())