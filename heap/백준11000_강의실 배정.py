import heapq
import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: x[0])

hq = []  

for start, end in arr:
    if hq and hq[0] <= start:
        heapq.heappop(hq) 
    heapq.heappush(hq, end)  
print(len(hq))  
