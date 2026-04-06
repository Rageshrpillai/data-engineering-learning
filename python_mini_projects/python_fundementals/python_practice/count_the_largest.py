l=[1,2,2,3,3,4,5]

def count_larg(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

print(count_larg(l))