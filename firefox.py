from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org")
driver.close
