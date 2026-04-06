Inputs ="hheeeelo"

def morethan(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    
    l=[]
    for key , Value in d.items():
        if Value > 1:
            l.append((key,Value))
    
    return l
    
    


print(morethan(Inputs))
            
    
#Shortcut
# use single line return statement insetead of last for loop like
# return [(k,v) for k , v in d.items() if v > 1]