s = "abcdeabcbbabcdefg"


def longestsub(s):
    maxcount=0
    start=0
    left=0
    seen={}
 

    for right in range(len(s)):
        
        seen[s[right]]=seen.get(s[right],0)+1

        while len(seen)>2:
            seen[s[left]]-=1
            if seen[s[left]]==0:
                del seen[s[left]]
            left+=1
        

        if right-left+1 > maxcount:
            start=left
            maxcount=right-left+1
    return s[start:start+maxcount] , len(seen ), maxcount


            

    
print(longestsub(s))