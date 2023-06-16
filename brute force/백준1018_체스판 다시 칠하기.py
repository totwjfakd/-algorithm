def chess_check(slice_chess) :
    change_count_w = 0
    change_count_b = 0
    CHESS_W = ['WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW']
    for row in range(8) :
        for col in range(8) :
            if slice_chess[row][col] != CHESS_W[row][col] :
                change_count_w += 1

    CHESS_B = ['BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',]
    for row in range(8) :
        for col in range(8) :
            if slice_chess[row][col] != CHESS_B[row][col] :
                change_count_b += 1
    
    return min(change_count_w, change_count_b)

N, M = map(int, input().split())
all_chess = [None for i in range(N)]

for i in range(N) :
    all_chess[i] = input()

min_num = 9999

set_row = N-7
set_col = M-7

for i in range(set_row) :
    for j in range(set_col) :
        slice_chess = []
        for k in range(8) :
            slice_chess.append(all_chess[i+k][j:j+8])
        
        change_num = chess_check(slice_chess)
        
        if change_num < min_num :
            min_num = change_num
print(min_num)