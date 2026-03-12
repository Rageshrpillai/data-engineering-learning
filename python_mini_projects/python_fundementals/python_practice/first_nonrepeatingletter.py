s="lleetcode"


#Declare a empty dic to add count for each letter
#main for loop to add character count to dic
# second for loop to find the unique char ( for loop in input string)



def first_longest(s):
    character_count={}
    for i in s:
        if i in character_count:
            character_count[i] +=1
        else:
            character_count[i]=1
    
    for i in s:
        if character_count[i]== 1:
            return i
        

print (first_longest(s))

         
