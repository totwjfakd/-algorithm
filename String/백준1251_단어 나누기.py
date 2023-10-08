str_ = input()

str_len = len(str_)
new_str = []
for i in range(1,str_len-1) :
    for j in range(i+1, str_len) :
        for k in range(j+1, str_len+1) :
            new_str.append(''.join([str_[:i][::-1], str_[i:j][::-1], str_[j:][::-1]]))
            
print(sorted(new_str)[0])