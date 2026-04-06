s=[1,2,2,3,3,4]

def dupli(s):
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    
    return l 

print(dupli(s))