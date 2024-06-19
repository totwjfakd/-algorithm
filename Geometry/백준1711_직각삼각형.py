import sys

input = sys.stdin.readline
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

def is_right_triangle(p1, p2, p3):
    u1, u2 = p2[0] - p1[0], p2[1] - p1[1]
    v1, v2 = p3[0] - p1[0], p3[1] - p1[1]
    
    dot_product1 = u1 * v1 + u2 * v2
    if dot_product1 == 0:
        return True
    
    u1, u2 = p3[0] - p2[0], p3[1] - p2[1]
    v1, v2 = p1[0] - p2[0], p1[1] - p2[1]
    
    dot_product2 = u1 * v1 + u2 * v2
    if dot_product2 == 0:
        return True
    
    u1, u2 = p1[0] - p3[0], p1[1] - p3[1]
    v1, v2 = p2[0] - p3[0], p2[1] - p3[1]
    
    dot_product3 = u1 * v1 + u2 * v2
    if dot_product3 == 0:
        return True

    return False

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_right_triangle(xy[i], xy[j], xy[k]):
                ans += 1

print(ans)
