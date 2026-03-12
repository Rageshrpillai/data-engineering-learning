# Input: "Hello world"
# Output: 2

def wordcount(s):
    words= s.split()
    return len(words)


s="Hello world ehuhu huhuh"
print (wordcount(s))