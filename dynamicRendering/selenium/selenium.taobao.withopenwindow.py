import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.debugger_address = 'localhost:9222'
# 免关闭
# options.add_experimental_option('detach', True)
# 防止window.navigator.webdriver 为true
# options.add_argument('--disable-blink-features=AutomationControlled')
# browser = webdriver.Chrome(options=options)
# browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)


def scrollBottom():
    '''
    把页面拉到底部
    :return:
    '''
    height = browser.execute_script("return document.body.scrollHeight")
    button = browser.find_element(By.XPATH, "//div[@class='next-pagination-list']/button[1]")
    by = button.location.get('y') - 100
    i = 100
    while height > i and by > i:
        browser.execute_script('window.scrollTo(0, ' + str(i) + ')')
        time.sleep(0.2)
        i = i + 100


def spiderData():
    divs = browser.find_elements(By.XPATH, "//div[@class='Content--contentInner--QVTcU0M']/div")
    for el in divs:
        print("title:" + el.find_element(By.XPATH, ".//div[@class='Title--title--jCOPvpf']/span").text)
        print("price:" + el.find_element(By.XPATH, ".//span[@class='Price--priceInt--ZlsSi_M']").text
              + el.find_element(By.XPATH, ".//span[@class='Price--priceFloat--h2RR0RK']").text)
        print("shop:" + el.find_element(By.XPATH, ".//a[@class='ShopInfo--shopName--rg6mGmy']").text)
        # print(el.text)


def next_page():
    # 1. 下一页
    button = browser.find_element(By.XPATH, "//button[@class='next-btn next-medium next-btn-normal next-pagination-item next-next']")
    by = button.location.get('y') - 100
    browser.execute_script('window.scrollTo(0, ' + str(by) + ')')
    time.sleep(5)
    browser.execute_script(
        'document.getElementsByClassName("next-pagination-pages")[0].getElementsByTagName("button")[1].click();')
    # 2. 把页面拉到最后面
    scrollBottom()
    # 3. 爬取数据
    spiderData()


def first_page():
    # 根据浏览器已经打开的窗口进行爬虫，打开的url为https://s.taobao.com/search?initiative_id=staobaoz_20231105&q=ipad
    # 把tab切换到最新的tab
    browser.switch_to.window(browser.window_handles[0])
    # 1. 把页面拉到最后面
    scrollBottom()
    # 2. 爬取数据
    spiderData()




first_page()

# 3. 下一页
for i in range(2, 11):
    next_page()
