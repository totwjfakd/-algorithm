T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if dist > r1 + r2 or dist < abs(r1 - r2):
        print(0)
        
    elif dist == 0 and r1 == r2:
        print(-1)
        
    elif dist < r1 + r2 and dist > abs(r1-r2) :
        print(2)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        print(1)