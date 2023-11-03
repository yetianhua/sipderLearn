from selenium import webdriver
from selenium.webdriver.common.by import By

def next_page(page):
    # 1. 把页面拉到最后面

    # 2. 爬取数据

    # 3. 下一页
    s = "/button[@class='next-btn next-medium next-btn-normal next-pagination-item'][" + str(page - 1) + "]"
    button = browser.find_element(By.XPATH, s)
    button.click()

options = webdriver.ChromeOptions()
# options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument(
#     'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)

browser.get('https://s.taobao.com')
print(browser.page_source)
# 1. 输入内容
input = browser.find_element(By.XPATH, "//input[@id='q']")
submit = browser.find_element(By.XPATH, "//button[@class='btn-search']")
input.clear()
input.send_keys("ipad")
submit.click()

# 2. 获取页面数据

# 3. 下一页
next_page(2)


