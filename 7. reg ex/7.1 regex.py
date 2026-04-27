# A regular expression (shortened as regex or regexp) is a sequence of characters that forms a specific search pattern.
# It is used for string-searching algorithms to find, replace, or validate text input.

# finding patterns without regex
def isPhoneNum(text) :
    if len(text) != 13:
        return False
    
    if text[0] != '+':
        return False
    
    if text[1:3] != '91':
        return False
    
    for i in range(3, 13):
        if not text[i].isdecimal():
            return False
        
    return True

print("+919876543210 is an Indian phone no.: ", isPhoneNum('+919876543210')) 
print("+90moshimoshi is an Indian phone no.: ", isPhoneNum('+90moshimoshi')) 
print("+909876543210 is an Indian phone no.: ", isPhoneNum('+909876543210')) 
print()



# with regular expression
import re                       # this is to make sure the regex will work

phoneNumRegex = re.compile(r'\+91\d{10}')
mo = phoneNumRegex.search('my phone no. is : +919876543210')
print(mo.group())

