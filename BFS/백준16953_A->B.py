from collections import deque

a, b = map(int, input().split())

queue = deque()

queue.append(a)
count = 1
while queue :
    queue_len = len(queue)
    
    for i in range(queue_len) :
        now = queue.popleft()
        if now > b :
            continue
        if now == b :
            print(count)
            exit()
        else :
            next_case1 = now*2
            next_case2 = int(str(now)+'1')


            queue.append(next_case1)

            queue.append(next_case2)
    count += 1
print(-1)