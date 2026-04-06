l=[1,2,3,4,5,6]

def divisble(l):
    s=[]
    for i in l:
        if i%2==0 and i%3==0:
            s.append(i)
    return s

print(divisble(l))

