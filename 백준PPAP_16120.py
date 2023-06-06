string = input()

stack = []

for c in string : 
    stack.append(c)
    ppap = ['P', 'P', 'A', 'P']
    if stack[-4:] == ppap :
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")
string = ''.join(stack)

if string == 'P' or string == "PPAP" :
    print("PPAP")
else :
    print("NP")