# phoneAndEmail.py --- Finds the phone number and email addresses on the clipboard

import pyperclip, re

# phone regex
phoneRegex = re.compile(r'''
    (?:\+\d+|0)?
    \d{10}
''', re.VERBOSE)


# email regex
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.
    [a-zA-Z]{2,}
''', re.VERBOSE)


# taking input from the clipboard and finding matches
text = pyperclip.paste()
matches = []

for group in phoneRegex.findall(text):
    matches.append(group)

for group in emailRegex.findall(text):
    matches.append(group)

print(matches)

# copying the output to the clipboard
if len(matches) > 0 :
    newText = '\n'.join(matches)
    pyperclip.copy(newText)
    print('Copied to clipboard')
    print(newText)
else:
    print("No phone numbers or email ids were availble in the text")



# example text to try (copy this):
# Rahul was organizing a tech meetup in Nagpur, so he shared his contact details (9876543210, +919812345678) and email (rahul.dev@gmail.com) with the team. 
# Meanwhile, Priya sent updates from her side via priya.work@company.in and asked everyone to reach her at 09876543210 if needed. 
# Later, the coordinator added another contact, support.team@event.org, and a backup number +917700112233 for emergencies.