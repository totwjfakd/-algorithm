num = int(input())
array = list(map(int, input().split()))
replay_num = int(input())
array.sort()
for i in range(replay_num) :
    array[0] += 1
    array[-1] -= 1
    array.sort()

print(array[-1] - array[0])