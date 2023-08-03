import heapq
import sys
heap = []

n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    num = int(sys.stdin.readline().rstrip())
    
    if num == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(-heapq.heappop(heap))
    else :
        heapq.heappush(heap, -num)
