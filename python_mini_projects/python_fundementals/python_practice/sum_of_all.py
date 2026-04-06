s=[1,2,3,4,5]

# def sumofall(s):
#     return sum(s)


# print(sumofall(s))


def primsum(s):
    total=0
    for i in s:
        if i%2==0:
            total+=i
    
    return total

print(primsum(s))