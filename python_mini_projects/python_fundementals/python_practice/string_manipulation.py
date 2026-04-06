s = "hello world"

def string_manupulation(data):
    l=data.split(" ")
    word=" ".join(l[::-1])
    
    return word
    


print(string_manupulation(s))