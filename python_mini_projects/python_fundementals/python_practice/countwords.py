s="heeeello"

def countwords(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    max=0
    largenum=0
    for key ,Value  in d.items():
        if Value > max:
            max=Value
            largenum=key
    
    return largenum
print(countwords(s))