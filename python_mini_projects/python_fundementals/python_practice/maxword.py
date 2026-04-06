# Input: "fun&!! time"
# Output: "time"
import re

def LongestWord(s):
  maxword=""
    # code here
  words = re.findall(r"[a-zA-Z]+",s)

   
  #largest number
  for word in words:
    if len(word)>len(maxword):
      maxword=word

  return maxword

s="funssss&!! time"
print (LongestWord(s))