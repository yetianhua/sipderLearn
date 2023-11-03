# Splash 是一个 JavaScript 渲染服务，是一个带有 HTTPAPI 的轻量级浏览器，同时它对接了 Python中的 Twisted 和 QT 库 。 利用它我们同样可以实现动态谊染页面的抓取 。

# Splash是一个纯JavaScript 渲染引擎，可以快速渲染动态网页，并且处理加载时间长的网页。 它适用于需要渲染动态内容的爬取任务。 而Selenium是一个自动化测试工具，可以模拟用户在浏览器中的操作，并且可以爬取动态网页内容。 但由于它是一个真正的浏览器，因此它比Splash慢得多

import requests
from urllib.parse import quote


# 1. 使用render.html来使用splash提供的http api接口, 此接口用于获取 JavaScript 渲染的页面的 HTML 代码
# url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
# response = requests.get(url)
# print(response.text)
# 使用wait参数
# url = 'http://localhost:8050/render.html?url=https://www.taobao.com&wait=5'
# response = requests.get(url)
# print(response.text)

# 2. render.png接口：此接口可以获取网页截图，其参数比 render.html 多了几个，比如通过 width 和 height 来控制宽高
# url = 'http://localhost:8050/render.png?url=https://www.baidu.com&width=1000&height=700'
# response = requests.get(url)
# with open('baidu.png', 'wb') as f:
#     f.write(response.content)

# 3. render.jpeg接口，此接口和 render.pug 类似，不过它返回的是 JPEG 格式的图片二进制数据 。

# 4. render.har接口：此接口用于获取页面加载的HAR数据
# url = 'http://localhost:8050/render.har?url=https://www.baidu.com&wait=5'
# response = requests.get(url)
# print(response.text)

# 5. render.json接口：此接口包含了前面接口的所有功能，返回结果是 JSON 格式,此外还有更多参数设置，具体可以参考官方文档：https://splash.readthedocs.io/en/stable/api.html#render-json
# url = 'http://localhost:8050/render.json?url=https://httpbin.org&wait=5&html=1&har=1'
# response = requests.get(url)
# print(response.text)

# 6. execute接口：前面的 render. html 和 render.png 等接口对于一般的 JavaScript 渲染页面是足够了 ，但是如果要实现一些交互操作的话，它们还是无能为力，这里就需要使用 execute 接口了 。
# lua = '''
# function main(splash)
#     return 'hello'
# end
# '''
# url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
# response = requests.get(url)
# print(response.text)

lua = '''
function main(splash)
    local treat = require("treat")
    local response = splash:http_get("https://httpbin.org/get")
    return {
        html = treat.as_string(response.body),
        url = response.url,
        status = response.status
    }
end
'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)