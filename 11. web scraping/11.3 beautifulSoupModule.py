# BeautifulSoup is a module for extracting info from an html page.

# we need to install the beautifulSoup module by:
# pip install beautifulsoup4

import requests, bs4

res = requests.get('https://sandeshlawhale.vercel.app')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)                                          # created a beautifulSoup object
print('type of soup: ' + str(type(soup)))


# finding an element with bs
# soup.select('name_of_the_element')              
# name_of_the_element                             will match
# div                                             all elements named div
# #author                                         the element with an id attribute of author
# .notice                                         All elements that uses css class attributenamed notice
# div span                                        elements named sapn that are inside div
# div > span                                      span that are directly inside div
# input[name]                                     elements named input that have a name attribute with any value
# input[type=button]                              all elements named input that have an attribute named type with value button


els = soup.select('div')
print(els[0].getText())
print(els[1].getText())
print(els[2].getText()[40:256])