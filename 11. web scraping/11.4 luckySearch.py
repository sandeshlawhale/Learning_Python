# luckySearch.py - Opens several google serach results

import requests, sys, webbrowser, bs4

print('googling...')
print(sys.argv[1])
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# retrive top search result
soup = bs4.BeautifulSoup(res.text, "html.parser")

#open browser for each tab
lineEls = soup.select('a')

numOpen = min(5, len(lineEls))
for i in range(numOpen):
    print(i, str(lineEls[i]))
    webbrowser.open('http://google.com'+ lineEls[i].get('href'))



# this is a basic version and this will get lot of error due to bot running detections