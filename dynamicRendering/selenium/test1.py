from selenium import webdriver
from selenium.webdriver import ActionChains

try:
    browser = webdriver.Chrome()
    url = 'https://www.w3school.com.cn/html/html5_draganddrop.asp'
    browser.get(url)
    source = browser.find_element_by_id('div1')
    target = browser.find_element_by_id('div2')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()

finally:
    browser.close()
