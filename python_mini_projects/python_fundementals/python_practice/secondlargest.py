s=[1,2,3,4,5]

#second largest


def secondlargest(s):
    second=sorted(s)

    return second[-2]
print(secondlargest(s))