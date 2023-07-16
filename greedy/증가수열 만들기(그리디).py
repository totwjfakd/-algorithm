from collections import deque

def left_pop() :
    global ans_num, ans, deq, ans_list
    ans_num += 1
    ans += 'L'
    
    ans_list.append(deq.popleft())

def right_pop() :
    global ans_num, ans, deq, ans_list
    ans_num += 1
    ans += 'R'
    
    ans_list.append(deq.pop())

n = int(input())

deq = deque(list(map(int, input().split())))

ans_num = 0
ans = ""
ans_list = []

for i in range(n) :
    if i == 0 :
        if deq[0] < deq[-1] :
            left_pop()
        else :
            right_pop()

    else :
        if deq[0] == deq[-1] and deq[0] > ans_list[-1]:
            left_pop()
        elif deq[0] > ans_list[-1] and deq[-1] > ans_list[-1] :
            if deq[0] < deq[-1] :
                left_pop()
            else :
                right_pop()
        elif deq[0] > ans_list[-1] :
            left_pop()
        elif deq[-1] > ans_list[-1] :
            right_pop()
        else :
            break

print(ans_num)
print(ans)
