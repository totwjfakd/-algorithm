def dfs(depth, make_string, start) :
    
    if depth == L :
        if len(set(make_string) & vowel_set) >= 1 and len(set(make_string) & consonant_set) >= 2:
            print(''.join(make_string))
        return
    for i in range(start, C) :
        if visit[i] :
            continue
        visit[i] = True
        dfs(depth+1, make_string+[alphabet[i]], i+1)
        visit[i] = False


L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
vowel_set = set(('a', 'e', 'i', 'o', 'u'))
consonant_set = set(('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'))
visit = [False for _ in range(C)]

dfs(0, [], 0)
