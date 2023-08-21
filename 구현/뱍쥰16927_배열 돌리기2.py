import math
import sys

def lotation(standard) :
    max_down_x = n-1-standard
    max_right_y = m-1-standard
    max_up_x = 0+standard

    for j in range(standard, max_down_x+1) :
        if j == standard :
            c = arr[j][standard]
        else :
            arr[j][standard], c = c, arr[j][standard]
    for j in range(standard+1, max_right_y+1) :
        arr[max_down_x][j], c = c, arr[max_down_x][j]
    for j in range(max_down_x-1, max_up_x-1, -1) :
        arr[j][max_right_y], c = c, arr[j][max_right_y]
    for j in range(max_right_y-1, standard-1, -1) :
        arr[standard][j], c = c, arr[standard][j]



n, m, r = map(int, sys.stdin.readline().rstrip().split())

arr = []


for i in range(n) :
    arr.append(list(sys.stdin.readline().rstrip().split()))

w = math.ceil(min(n, m)/2)

r_list = [[] for _ in range(w)]

for i in range(0, w) :

        r_list[i] = ((n-(2*i)-1)+(m-(2*i)-1))*2
    
for i in range(w) :
    for q in range(r%r_list[i]) :
        lotation(i)

for l in arr :
    print(' '.join(l))