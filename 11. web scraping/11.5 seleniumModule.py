# The selenium module lets python direcltly control the browser by programmatically clicking links and filling in login information, almost as though there is a human user interacting with the page.
# Selenium allows you to interact with web pages in a much more advanced way than requests and bs4.

# In this project we will make sure to fetch the products from the amazon websites

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.chdir('.\\11. web scraping')
os.makedirs('data', exist_ok=True)

driver = webdriver.Chrome()                            # by doing this we starts the browser, we can also use different browsers
print('type of driver: '+ str(type(driver)))

query = 'laptop'
fileno = 1
driver.get(f'https://www.amazon.in/s?k={query}&crid=367OQZL0JHZYI&sprefix=lapto%2Caps%2C347&ref=nb_sb_noss_2')         # this redirects the browser page to this link

try:                                                                                    # handles errors gracefully instead of crashing the program
    elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')                  # fetching the element form the page

    for elem in elems:                                                                  # looping over all the elements that found
        data = elem.get_attribute('outerHTML')                                          # gets complete HTML of the current product card
        with open(f'data/{query}_{fileno}.html', 'w', encoding='utf-8') as f:           # creating new html file in side the data folder
            f.write(data)                                                               # writing the html to the newly created file

        fileno += 1

except Exception as e:
    print('was not able to find the element: ', e)

driver.quit()                                                                   