# Input: "All cows eat grass"
# Output: 5

def vowels(s):
    vow=["a","e","i","o","u"]
    count=0

    for char in s.lower():
        if char in vow:
            count+=1
    
    return count


s="All cows eat grass"
print (vowels(s))