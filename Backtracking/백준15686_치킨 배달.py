import sys

def make_combination(select_count, select_xy, visit, start) :
    global combination
    if select_count == m :
        combination.append(select_xy)
    
    for i in range(start, len(chicken_xy)) :
        if visit[i] :
            continue
        visit[i] = True
        make_combination(select_count+1, select_xy+[chicken_xy[i]], visit, i+1)
        visit[i] = False

input = sys.stdin.readline

n, m = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(n)]

chicken_xy = []
home_xy = []
for i in range(n) :
    for j in range(n) :
        if map_[i][j] == 2 :
            chicken_xy.append((i,j))
        elif map_[i][j] == 1:
            home_xy.append((i,j))

combination = []
visit = [False for _ in range(len(chicken_xy))]

make_combination(0, [], visit, 0)

ans = 9999999
for chicken_ in combination :
    sum_ = 0
    for home_ in home_xy :
        min_ = 99999
        for tuple_ in chicken_ :
            minus = abs(tuple_[0] - home_[0]) + abs(tuple_[1] - home_[1])
            if min_ > minus :
                min_ = minus
        sum_ += min_
    if sum_ < ans :
        ans = sum_
print(ans)