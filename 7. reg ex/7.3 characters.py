# characters in regex

# shorthands              Represents
# \d                      Any number digit from 0-9
# \D                      Any char that is not a numeric digit form 0-9
# \w                      Any letter, numeric digit or the underscore character (word)
# \W                      Anything other than letter, numeric digit or the underscore character
# \s                      Any space, tab or new line character
# \S                      Anything other than space, tab or new line character

import re

print("using the shortands for the characters in regex:")
xmasRegex = re.compile(r'\d+\s\w+')                         #\d+\s\w+ means one or more digits, one space and one or more words
mo = xmasRegex.findall('12 drums'+ '5 rings'+ '11 pipers'+ '10 lords'+ '9 ladies')
print(mo)


# caret and doller sign character
# caret symbol (^) at the start of a regex to indicate that a mcatch must occur at teh beginning of teh searched text.
# like wise, you can use dollar sign($) at teh end of the regex to indicate this string must end witht his regex pattern.
print("\nusing caret:")
beginWithHello = re.compile(r'^hello')
mo = beginWithHello.search('hello world!')
print(mo)

mo1 = beginWithHello.search('is it starts with hello world!')
print(mo1)


print('\nusing dollar sign:')
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('your number is 42'))
print(endsWithNumber.search('your number is forty two'))


print('\nstarts with caret and ends with dollar:')
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('123456789'))
print(wholeStringIsNum.search('1234ghi6789'))



# wild card character (.)
# the . (dot) character in a regular expression is called a wildcard and will match any character except for a new line.

print('\nusing the . wildcard character')
atRegex = re.compile(r'.at')
print(atRegex.findall('the cat in teh hat sat on the flat mat.'))


# matching everything with dot star (.*)
print('\nmatching everything with dot star(.*)')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Sandesh Last Name: Lawhale')
print(mo.groups())


# matching newline with the dot character
print('\nnewline with dot')
noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('server the public trust.\nprotext the innocent.\nuphold the law.').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('server the public trust.\nprotext the innocent.\nuphold the law.').group())



# case sensetive matching with re.I or re.IGNORECASE
print("\ncase-sensitive matching with re.I")
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, prt machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())



# substituting string with sub method
print('\n sub method to substitute')
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))


agentNameRegex = re.compile(r'Agent (\w)\w*')
print(agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent'))


# managing complex regexes
# using re.VERBOSE
# with the help of verbose we can use white spaces and comments in regex

print('\nRe.verbose')
phoneRegex = re.compile(r'''
    \+91            #EXTENSION 
    (\d){10}        # 10 digits
''', re.VERBOSE)
print(phoneRegex.search("is this a valid no. : +919876543210"))





