from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Selenium 支持非常多的浏览器，如 chrome Firefox Edge
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.Safari()


# 2. 访问页面
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# print(browser.page_source)
# browser.close()

# 3. 查找节点 我们想要完成向某个输入框输入文字的操作，总需要知道这个输入框在哪里吧
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# input1 = browser.find_element(By.ID, 'q')
# input2 = browser.find_element(By.CSS_SELECTOR, '#q')
# input3 = browser.find_element(By.XPATH, '//*[@id="q"]')
# print(input1, input2, input3)
# list = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(list)
# browser.close()

# 4. 节点交互 更多的操作可以参见官方文档的交互动作介绍： http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# input = browser.find_element(By.ID, 'q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element(By.CLASS_NAME, 'btn-search')
# button.click()
# browser.close()

# 5. 动作链 在上面的实例中，一些交互动作都是针对某个节点执行的。 其实，还有另外一些操作，它们没有特定的执行对象，比如鼠标拖曳 键盘按键等，这些动作用另一种方式来执行，那就是动作链
# 5.1 现在实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处
# browser = webdriver.Chrome()
# browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# # focus to the specified frame
# browser.switch_to.frame('iframeResult')
# source = browser.find_element(By.CSS_SELECTOR, '#draggable')
# target = browser.find_element(By.CSS_SELECTOR, '#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 6. 执行javascript 对于某些操作， Selenium API 并没有提供 比如，下拉进度条，它可以直接模拟运行 JavaScript
# option是防止代码执行完，浏览器自动关闭
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# browser = webdriver.Chrome(options=option)
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Button")')

# 7. 获取节点信息，通过 page_source 属性可以获取网页的源代码，接着就可以使用解析库（Beautiful Soup pyquery等）
# 不过，既然Selenium已经提供了选择节点的方法，返回的是Web Element类型，那么它也有相的方法和属性来直接提取节点信息
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# browser = webdriver.Chrome(options=option)
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element(By.CLASS_NAME, 'ExploreHomePage-ContentSection-header')
# # 获取属性
# print(logo)
# print(logo.get_attribute('class'))
# # 获取文本
# input = browser.find_element(By.CLASS_NAME, 'ExploreHomePage-ContentSection-header')
# print(input.text)

# 8. 切换frame 略，详情请看5

# 9. 延时等待 get （）方法会在网页框架加载结束后结束执行，此时如果获取 page_source ，可能
# 并不是浏览器完全加载完成的页面，如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不
# 定能成功获取到 所以，这里需要延时等待一定时间，确保节点已经加载出来

# 9.1 隐式等待 使用隐式等待执行测试的时候，如果 Selenium 没有在 DOM中找到节点，将继续等待，
# 如果超出设定时间后，则抛出找不到节点的异常
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# browser = webdriver.Chrome(options=option)
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element(By.CLASS_NAME, 'ExploreHomePage-ContentSection-header')
# print(logo)
# 9.2 显式等待 显式等待方法，它指定要查找的节点，然后指定一个最长等待时间 如果
# 在规定时间内加载出来了这个节点，就返回查找的节点，如果到了规定时间依然没有加载出该节点，
# 则抛阳超时异常
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# # 查找内容可被定位
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# # 查找内容可被点击
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 10. 前进和后退 平常使用浏览器时都有前进和后退功能， Selenium 也可以完成这个操作，它使用back()方法后退，
# 使用于forward()方法前进
# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# browser = webdriver.Chrome(options=option)
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()

# 11. Cookies 使用 Selenium ，还可以方便地对 Cookies 进行操作，例如获取 添加 删除 Cookies
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

