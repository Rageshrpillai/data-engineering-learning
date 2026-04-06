s=[10, 15, 20, 25]

def greaterthan(s):
    l=[]
    for i in s:
        if i >= 15:
            l.append(i)
    
    return l

print(greaterthan(s))