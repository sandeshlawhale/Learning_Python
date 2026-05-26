#! python3
# mcb.py - multiclipboard - saves and loads pieces of text to clipboard
# usage:    py.exe mcb.py save <keyword> - saves the clipboard to keyword
#           py.exe mcb.py delete <keyword> - delete the value of the keyword
#           py.exe mcb.py <keyword> - loads the keyword value to clipboard
#           py.exe mcb.py list - loads all keyword to clipboard
#           py.exe mcb.py clear - clears all the keywords 

import shelve, pyperclip, sys

# open the file as shelf
mcbShelf = shelve.open('8. read and write files\\sample\\mcb')

if len(sys.argv) == 3:
    keyword = sys.argv[2]
    if sys.argv[1].lower() == 'save':
        # save clipboard content
        mcbShelf[keyword] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        # delete keyword from clipboard content
        del mcbShelf[keyword]
elif len(sys.argv) ==2:
    cmd = sys.argv[1]
    if cmd.lower() == 'clear':
        # clear all clipboard content
        mcbShelf.clear()
    elif cmd.lower() == 'list':
        # list keywords and load content
        keys = str(list(mcbShelf.keys()))
        pyperclip.copy(keys)
    elif cmd in mcbShelf.keys():
        pyperclip.copy(mcbShelf[cmd])

