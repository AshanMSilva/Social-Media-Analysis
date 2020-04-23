import pickle
import selenium.webdriver 

driver = selenium.webdriver.Chrome()
driver.get("http://www.facebook.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)