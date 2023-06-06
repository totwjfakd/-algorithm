def check_left_wall(idx, world) :
    for k in range(idx-1, -1, -1) :
        if world[k] > world[idx] :
            return True
    return False

def check_right_wall(idx, world) :
    for k in range(idx+1, len(world), 1) :
        if world[idx] < world[k] :
            return True
    return False


h, w = map(int, input().split())
world = list(map(int, input().split()))
rain_water = 0

for i in range(1, w-1, 1) :
    while check_left_wall(i, world) and check_right_wall(i, world) :
        world[i] += 1
        rain_water += 1
    print(world)

print(rain_water)