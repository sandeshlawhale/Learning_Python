# The requests module lets you easily download files from the web without having to worry about the complicated issues such as network errors, connnection problems and data compressions

# requests module doesn't come with python so we have to install it by:
# pip install requests

import requests

res = requests.get('https://sandeshlawhale.vercel.app')                                     # made a request to download the page
print("type of res: " + str(type(res)))                                                 

# if res.status_code == requests.codes.ok:                                                    # always check status to make sure the download is completed
#     print('len of the downloaded text: '+ str(len(res.text)))
#     print("text: " + res.text[2200:2500])


# there are better ways for checking the errors 
# res.raise_for_status()                                                            # add this line always after the res, to make sure the page downloaded successfully
                                                                                    # and for better, add this in try except block to make sure the program wont terminate

try: 
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

downloadedFile = open('.\\11. web scraping\\downloadedFile.txt', 'wb')                 # to write a downloadable content to file
for chunk in res.iter_content(100000):                                                                  # better use chunks, and 100000 is enough for a single chunk
    downloadedFile.write(chunk)