from collections import deque

def BFS(start) :
    queue = deque()
    queue.append(start)

    ch = [0] * (MAX+1)

    ch[S] = 1

    while queue :
        now = queue.popleft()
        if now == E :
            break
        for next in (now-1, now+1, now*2) :
            if 0<=next<=MAX :
                if ch[next] == 0 :
                    ch[next] = 1
                    dis[next] = dis[now] + 1
                    queue.append(next)

    
    
MAX = 100000

S, E = map(int, input().split())
dis = [0] * (MAX+1)

BFS(S)
print(dis[E])