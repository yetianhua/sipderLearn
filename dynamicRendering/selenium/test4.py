from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://s.taobao.com/")
