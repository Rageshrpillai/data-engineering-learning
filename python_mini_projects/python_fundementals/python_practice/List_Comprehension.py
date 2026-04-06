l = [1,2,3,4,5,6]

s = [4,5,6,7,8,9,10,11,12]


def listcomp(data):
        result =[x for x in data if x%2==0]
        return result


print(listcomp(l))
print(listcomp(s))