from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.taobao.com")
input = browser.find_element(By.ID, 'q')
input.send_keys('iPhone')
input.clear()
input.send_keys('iPad')
button = browser.find_element(By.CLASS_NAME, 'btn-search')
button.click()
browser.close()