import re
# grouping with parentheses

phoneNumRegex = re.compile(r'(\+91)(\d{10})')
mo = phoneNumRegex.search("my phone number is +918765432109")
print(mo.group())                               # generally return the 0th group that is the whole find
print(mo.group(0))                              
print(mo.group(1))                              # returns the first goup and so on
print(mo.group(2))
print(mo.groups())                              # returns all groups available as touple

# destrucuring the groups
areacode, phonenum = mo.groups()
print("areacode: ", areacode, " phonenum: ", phonenum)


# matching multiple groups with pipe 
# | this character is called pipe 

print('\nmatching multiple groups with pipe')
heroRegex = re.compile(r'batman|tina fey')
mo1 = heroRegex.search('batman and tina fey')
print(mo1.group())

mo2 = heroRegex.search('tina fey and batman')
print(mo2.group())

mo3 = heroRegex.findall('tina fey and batman')
print(mo3)



# optional matching with question mark

print('\noptional matching with question mark:')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventure of the Batman')
print(mo1.group())

mo1 = batRegex.search('The Adventure of the Batwoman')
print(mo1.group())



# matching zero or more with starts
print('\nmatching zero or more with star:')

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of the Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of the Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventure of the Batwowoman')
print(mo3.group())



# matching one or more with plus

print('\nmatching one or more with plus:')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventure of the Batman')
print(mo1)                                                          # match will be none here, as the plus need atleast one occurance

mo2 = batRegex.search('The Adventure of the Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventure of the Batwowoman')
print(mo3.group())


# matching specific repeatation with curly brackets
# in curly brackets if you only pass 3 it will check for 3 repeatation only
# and if you pass two numbers like {3,5} it will check for atleast 3 to atmost 5
# and if you did not mention the first number it will start from 0 till the next number
#  vise versa if you did not mention the next number

print("\nspecific repeatation with curly brackets: ")
batRegex = re.compile(r'(HA){3}')
mo1 = batRegex.search('HAHAHA')
print(mo1.group())                                                          # match will be none here, as the plus need atleast one occurance

mo2 = batRegex.search('HA')
print(mo2)



# greedy and non greddy matching 
# non greedy matching is performed with question mark and it returns the least matching string
# by default every match is greedy

print('\nnon greedy matching:')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHa')
print(mo2.group())



# find all method
# use to find the all occurrance or matches

print('\nfindall method:')
mo = phoneNumRegex.search('cell: +919876543210 work: +911234567890')
print(mo.group())

mo1 = phoneNumRegex.findall('cell: +919876543210 work: +911234567890')
print(mo1)
# in the above findall example we use the regex with parentheses groups that will give the answer in the touple of the strings
# if we use normal regex without groups it will give the simple array of strings like this
# ['919876543210','911234567890']



