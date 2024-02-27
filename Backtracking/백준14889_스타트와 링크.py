import sys
import itertools

input = sys.stdin.readline

n = int(input())
map_ = []
for i in range(n) :
    map_.append(list(map(int, input().split())))


arr = [i for i in range(1, n+1)]

all = list(itertools.combinations(arr, n//2))

min_ = 99999
for tuple_ in all :
    arr2 = arr[:]
    for num in tuple_ :
        del arr2[arr2.index(num)]
    
    team_a = 0
    team_b = 0
    
    team_a_permutation = list(itertools.permutations(list(tuple_), 2))
    team_b_permutation = list(itertools.permutations(arr2, 2))
    
    for i, j in team_a_permutation :
        team_a += map_[i-1][j-1]
    for i, j in team_b_permutation :
        team_b += map_[i-1][j-1]

    if abs(team_a-team_b) < min_ :
        min_ = abs(team_a-team_b)
print(min_)

