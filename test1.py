from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
((JavascriptExecutor) webDriver).executeScript("window.focus();");
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
time.sleep(2)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()