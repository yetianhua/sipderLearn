# urllib库，它是Python内 置的HTTP 请求库
import urllib.request

import urllib.parse

# urllib错误模块
import urllib.error

import socket

# 1. urlopen() 利用最基本的 urlopen()方法，可以完成最基本的简单网页的 GET 请求抓取。
#response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

# 2. 响应类型
#response = urllib.request.urlopen('https://www.python.org')
# print(type(response)) # <class’http.client.HTTPResponse’ >
# 可以发现，它是一个HTTPResposne 类型的对象，主要包含 read（）、readinto（）、getheader(name ）、 gethea ders（）、fileno（）等方法，以及msg、version、status、reason、debuglevel、ιlosed等属性。

# 3. response的一些属性、方法
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))

# 4. 使用urlopen传递参数
#data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding = 'utf-8')
#response = urllib.request.urlopen('http://httpbin.org/post', data=data)
#print(response.read().decode('utf-8'))

# 5. timeout 参数
# response = response = urllib.request.urlopen('http://httpbin.org/get', timeout=1) # 这里我们设置超时时间是l秒
# print(response.read().decode('utf-8'))

# 6. 使用try except语句抓取错误
# try:
#     response = response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except BaseException as e:
#     print(e)

# 7. 其他参数
# context 参数，它必须是 ssl.SSLContext类型，用来指定 SSL 设置。
# cafile 和 ca path 这两个参数分别指定 CA 证书和它的路径，这个在请求HTTPS 链接时会 有用。
