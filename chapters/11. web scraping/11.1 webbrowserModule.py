# webbrowser module's open() function can launch the new browser to a specified url.

import webbrowser, sys, pyperclip
# webbrowser.open('https://sandeshlawhale.vercel.app/')

# let's write a code to open a map location in a web browser
baseMapUrl = 'https://www.google.com/maps/place/'

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else :
    address = pyperclip.paste()

print('searching ' + address + "...")
webbrowser.open(baseMapUrl + address)

