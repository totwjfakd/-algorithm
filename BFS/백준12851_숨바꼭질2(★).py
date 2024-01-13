from collections import deque

a, b = map(int, input().split())

queue = deque()
queue.append(a)
visit = [0 for _ in range(100001)]
sec_count = 0
ans_count = 0
count = 0
while queue :
    len_queue = len(queue)
    for i in range(len_queue) :
        now = queue.popleft()
        if now == b :
            sec_count = count
            ans_count += 1
            continue

        for next in (now-1, now+1, now*2) :
            if (next >= 0 and next <=100000) and (visit[next] == 0 or visit[next] == visit[now] + 1) :
                visit[next] = visit[now] + 1
                queue.append(next)
    count += 1

print(sec_count)
print(ans_count)
