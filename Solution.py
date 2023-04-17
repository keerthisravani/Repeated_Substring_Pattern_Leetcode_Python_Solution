def repeatedSubstringPattern(s):
    result=""
    if len(s)==1:
        return False
    for i in range((len(s)//2)):
        result=result+s[i]
        n=len(result)
        rem_str=s[i+1:]
        coun=rem_str.count(result)
        if n*coun==len(rem_str):
            return True
    return False
s="abab"
print(repeatedSubstringPattern(s))