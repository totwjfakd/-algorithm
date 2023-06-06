
string_change = False
def find_ppap(string) :
    global string_change 
    for i in range(0, len(string)-3, 1) :
        if string[i:i+4] == "PPAP" :
            string_change = True
            return string[:i] + 'P' + string[i+4:]

      
string = input()


while True :
    string = find_ppap(string)
    if not string_change or not string:
        print("NP")
        break
    if string == "P" :
        print("PPAP")
        break
    