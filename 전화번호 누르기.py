import math

num_d = [['1', '2', '3'],
         ['4', '5', '6'], 
         ['7', '8', '9'], 
         ['*', '0', '#']]

index_dict = {}

for i in range(4) :
    for j in range(3) :
        index_dict[num_d[i][j]] = [i, j]

command_line = input().split()
commnad_hand = input()

left_hand = index_dict['*']
right_hand = index_dict['#']

res = ""
for i in command_line :
    if i == '1' or i == '4' or i == '7' :
        res += 'L'
        left_hand = index_dict[i]
    elif i == '3' or i == '6' or i == '9' :
        res += 'R'
        right_hand = index_dict[i]
    
    else :
        l_h_len = abs(index_dict[i][0] - left_hand[0]) + abs(index_dict[i][1] - left_hand[1])
        r_h_len = abs(index_dict[i][0] - right_hand[0]) + abs(index_dict[i][1] - right_hand[1])

        if r_h_len == l_h_len :
            if commnad_hand == 'right' :
                res += 'R'
                right_hand = index_dict[i]
            else :
                res += 'L'
                left_hand = index_dict[i]
        elif r_h_len > l_h_len :
            res += 'L'
            left_hand = index_dict[i]
        else :
            res += 'R'
            right_hand = index_dict[i]
print(res)