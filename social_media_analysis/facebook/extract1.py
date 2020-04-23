import pickle
import selenium.webdriver 
import time

driver = selenium.webdriver.Chrome()
# driver.get("http://www.facebook.com")
time.sleep(10)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


