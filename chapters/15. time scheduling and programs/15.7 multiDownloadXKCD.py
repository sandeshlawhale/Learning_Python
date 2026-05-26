# Project: Multithreaded XKCD Downloader
# This program downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading

os.chdir('.\\15. time scheduling and programs')

# Create folder to store comics
os.makedirs('xkcd', exist_ok=True)

# Function to download comics
def downloadXkcd(startComic, endComic):

    for urlNumber in range(startComic, endComic):

        # Download page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))

        res = requests.get('https://xkcd.com/%s' % (urlNumber))

        res.raise_for_status()

        # Parse HTML page
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find comic image
        comicElem = soup.select('#comic img')

        if comicElem == []:

            print('Could not find comic image.')

        else:

            # Get image URL
            comicUrl = 'https:' + comicElem[0].get('src')

            # Download image
            print('Downloading image %s...' % (comicUrl))

            res = requests.get(comicUrl)

            res.raise_for_status()

            # Save image
            imageFile = open(
                os.path.join(
                    'xkcd',
                    os.path.basename(comicUrl)
                ),
                'wb'
            )

            # Save image in chunks
            for chunk in res.iter_content(100000):

                imageFile.write(chunk)

            imageFile.close()

# Store thread objects
downloadThreads = []

# Create and start threads
for i in range(0, 140, 10):

    downloadThread = threading.Thread(
        target=downloadXkcd,
        args=(i, i + 9)
    )

    downloadThreads.append(downloadThread)

    downloadThread.start()

# Wait for all threads to finish
for downloadThread in downloadThreads:

    downloadThread.join()

print('Done.')