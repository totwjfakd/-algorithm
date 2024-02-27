from collections import deque

N, T, G = map(int, input().split())

queue = deque()

queue.append(N)
count = 0
visit = [0 for _ in range(100000)]
visit[N] = 1
while queue :
    if count > T:
        print("ANG")
        exit()
    queue_len = len(queue)
    
    for _ in range(queue_len) :
        now = queue.popleft()

        if now == G :

            print(count)
            exit()

        if now+1 <= 99999 :
            a_button = now + 1
            if visit[a_button] == 0 :
                visit[a_button] = 1
                queue.append(a_button)

        if 0 < now*2 <= 99999 :
            b_button = list(map(int, list(str(now*2))))
            b_button[0] -= 1
            b_button = int(''.join(list(map(str, b_button))))


            if visit[b_button] == 0 :
                visit[b_button] = 1
                queue.append(b_button)
    count += 1
print("ANG")
