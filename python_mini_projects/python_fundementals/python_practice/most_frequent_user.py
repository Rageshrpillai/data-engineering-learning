s=  [1,1,2,2,2,3,3,4,5]

def most_frequent_user(users):

    #edge case if the input is none
    if not users:
        return None

    dc={}
    count=-1
    result=None

    for i in users:
        if i in dc:
            dc[i]+=1
        else:
            dc[i]=1
    
    for key ,value in dc.items():
        if value > count:
            result=key
            count=value
        elif value == count:
            result=min(result,key)
    
    return result



        
                

print(most_frequent_user(s))


#loop thorugh list and add a count for each

#Then return longest count by using loop if it tie compare the value
