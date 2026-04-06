i=[1,2,2,3,3,4]

def xorcon(l):
    result=[]
    for i in l:
        if (i%2==0 or i%3==0)and not ( i%3==0 and i%2==0):
            result.append(i)
    return print(result)

xorcon(i)