def change(binary) :
    pass


num = input()
b_list = []
o_list = []
d_list = []
h_list = []

b_str = ""


for i in range(len(num)) :
    b_str += num[i]

    if i % 8 == 7 :
        b_list.append(b_str)
        b_str = ""


b_res = ".".join(b_list)

print(b_res)




for i in b_list :
    o_num = 1
    o_int = 0
    o_count = 0
    o_str = ""
    for j in range(len(i)-1, -1, -1) :
        if i[j] == '1' :
            o_int += o_num
        o_count += 1
        o_num *= 2
        if o_count == 3 :
            o_str += str(o_int)
            o_num = 1
            o_count = 0
            o_int = 0
        if j == 0 :
            o_str += str(o_int)
    o_str = int(o_str[::-1])

    
    o_list.append(str(o_str))

o_res = ".".join(o_list)
print(o_res)            


d_res = ""
for i in b_list :
    d_num = 1
    d_int = 0
    for j in range(len(i)-1, -1, -1) :
        if i[j] == '1' :
            d_int += d_num
        d_num *= 2

    d_list.append(str(d_int))

d_res = ".".join(d_list)

print(d_res)

for i in b_list :
    h_num = 1
    h_int = 0
    h_count = 0
    h_str = ""
    for j in range(len(i)-1, -1, -1) :
        if i[j] == '1' :
            h_int += h_num
        h_count += 1
        h_num *= 2
        if h_count == 4 :
            if h_int >= 10 :
                h_str += str(format(h_int, 'x'))
            else :
                h_str += str(h_int)
            h_num = 1
            h_count = 0
            h_int = 0

    h_str = h_str[::-1]
    if h_str[0] == '0' :
        h_str = h_str[1]
        
    
    #h_str = int(h_str[::-1])

    
    h_list.append(str(h_str))

h_res = ".".join(h_list)
print(h_res)            