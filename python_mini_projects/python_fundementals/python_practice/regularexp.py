import re

l="@SAC$E%SS**12NK"

def regular(l):
    s=re.findall("[a-zA-Z]+",l)
    result="-".join(s)
    return print(result)

regular(l)

