#input = "ABCD"
#output = "BCDE"

def nextword(s):
    word=""
    #loop through each char in string to find the next word
    for char in s:
        if char in 'zZ':
            word+="a"if char == 'z' else 'A'
        else:
            word+=chr(ord(char)+1)
             
    
    return word

    #convert the input to asci code then  add  +1  then convert back to char


s="Zxyc"
print(nextword(s))