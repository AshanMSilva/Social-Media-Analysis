import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get('https://www.facebook.com')
time.sleep(30)  # Time to enter credentials
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
driver.get('https://www.facebook.com/kavinga.lankari.5')  # Already authenticated
time.sleep(10)
driver.quit()