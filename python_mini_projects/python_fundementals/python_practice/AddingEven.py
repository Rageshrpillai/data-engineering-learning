def addingnum():
    l = []
    for i in range(1, 6):
        if i%3==0:
            l.append(i)
    return l

print(addingnum())