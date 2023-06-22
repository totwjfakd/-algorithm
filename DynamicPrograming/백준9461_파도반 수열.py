dp_arr = [0 for _ in range(101)]

dp_arr[0] = 1
dp_arr[1] = 1
dp_arr[2] = 1

for i in range(3, 101, 1) :
    dp_arr[i] = dp_arr[i-3] + dp_arr[i-2]


t = int(input())

for i in range(t) :
    print(dp_arr[int(input())-1])