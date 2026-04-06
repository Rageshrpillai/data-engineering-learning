s = "banana"

def frequency(data):
    s={}
    for i in data:
        s[i]= s.get(i , 0 )+1
    return s

print (frequency(s)) 

#dic comprehension

# s={i: data.count(i) for i in data }