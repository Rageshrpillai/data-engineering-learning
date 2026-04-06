l=[1,2,6,4,5]

def largestnum(l):
    maxs=l[0]
    for i in l:
        if i < maxs:
            maxs=i
    return maxs

print(largestnum(l))