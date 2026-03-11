# Input: "fun&!! time"
# Output: "time"
import re

def LongestWord(s):
    # code here
    words=re.findall(r"[a-zA-Z]+",s)

    print(words)

    # maxword=max(word , key=len)
    # print(maxword)
    maxword=''
    for word in words:
        if len(word) > len(maxword):
            maxword = word
    return maxword;

s="fun&!! time"
print (LongestWord(s))