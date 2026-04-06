l=[1,2,3,4,5,6,7]
target=7


# def twosum(target,l):
#     d=[]
#     for i in range(len(l)):
#         print(i)
#         for j in range(i+1,len(l)):
#             print(i,j)
#             if l[i]+l[j] == target:
#                 d.append((l[i],l[j]))
    
#     return d


def twosumfast(target,l):
    seen=set()
    result=[]

    for num in range(len(l)):
        need=target-l[num]
        if need in seen:
            result.append((l[num],need))
        seen.add(l[num])
    return result


print(twosumfast(target,l))


