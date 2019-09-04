from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("start-maximized")

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.facebook.com/login')

time.sleep(2)

# LOGIN
email = browser.find_element_by_id('email')
email.send_keys('your email' + Keys.TAB)

password = browser.find_element_by_id('pass')
password.send_keys('your password' + Keys.RETURN)

# Go to Page Fans
pageId = 'id'
browser.get('https://www.facebook.com/search/{}/likers?ref=about'.format(pageId))

fb = browser.find_element_by_id('facebook')

# Scrool down to load more users
for i in range(100):
    fb.send_keys(Keys.END)
    time.sleep(5)

urls = browser.find_elements_by_css_selector('._32mo')

# Assign the profile url for each user
usersList = []

for url in urls:
    user = str(url.get_attribute('href'))
    urlSplit = user.split("/")
    id = urlSplit[3]
    listID = id.split("?")
    id = listID[0]
    usersList.append(id)


for user in usersList:
    print(user)
