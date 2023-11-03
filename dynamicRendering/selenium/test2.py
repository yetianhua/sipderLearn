from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

try:
    browser = webdriver.Chrome()
    url = 'https://www.baidu.com'
    browser.get(url)
    browser.get("https://www.baidu.com")
    input = browser.find_element(By.ID, 'kw')
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # 实际执行script
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
finally:
    print('hhhh')