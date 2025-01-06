def aa():
    for i in range(4):
        if dist[0] != dist[i]:
            print(0)
            return
            
    if dist[4] != dist[5]:
        print(0)
        return
    print(1)



t = int(input())

for _ in range(t):
    dist = []
    arr = []
    for j in range(4):
        arr.append(list(map(int, input().split())))
    
    for i in range(4):
        for j in range(i+1, 4):
            dist.append(((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**0.5)
    dist.sort()

    aa()