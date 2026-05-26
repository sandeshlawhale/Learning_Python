# regexStrip.py - a regex program that strips the string

import re

def regex_strip(text, char=None):
    if char==None:
        spaceRegex = re.compile(r'^\s+|\s+$')
        mo = spaceRegex.sub("",  text)
    else:
        charRegex = re.compile(rf'^[{char}]+|[{char}]+$')
        mo = charRegex.sub("", text)
    
    print(mo)



regex_strip("   hello   ")
regex_strip("xxxhelloxxx", "x")
regex_strip("xyxyxyhelloxyxyxy", "xy")

