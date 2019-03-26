from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import re

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/login')

time.sleep(2)

# LOGIN
email = browser.find_element_by_id('email')
email.send_keys('marcelogrsp@hotmail.com' + Keys.TAB)

password = browser.find_element_by_id('pass')
password.send_keys('rVAnERxXjtng2Md!' + Keys.RETURN)

# Go to Page Fans
browser.get('https://www.facebook.com/search/160996273912155/likers?ref=about')

time.sleep(2)

fb = browser.find_element_by_id('facebook')

for i in range(5):
    fb.send_keys(Keys.END)
    time.sleep(2)

contacts = browser.find_elements_by_css_selector('._32mo span')

for contact in contacts:
    print(contact.text)

time.sleep(4)

# urls = browser.find_elements_by_partial_link_text('https://www.facebook.com/')
urls = browser.find_elements_by_css_selector('._32mo')

for url in urls:
    user = url.get_attribute('href')
    print(user)
    p = re.compile(.*\/(.*)\?)
    print(p)