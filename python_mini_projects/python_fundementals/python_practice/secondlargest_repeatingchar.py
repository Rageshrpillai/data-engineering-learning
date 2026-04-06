Inputs ="heeeello"

def secondlargest(s):
    a={}
    for i in s:
        a[i]=a.get(i,0)+1
    sort=sorted(a.items(),key=lambda x:x[1])
    return sort[-1] ,sort[-2]

print(secondlargest(Inputs))
