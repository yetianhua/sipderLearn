from socket import socket

import requests
import socks

# 1. requests 使用http代理
# proxy = '127.0.0.1:7078'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'http://' + proxy,
# }
#
# response = requests.get("http://httpbin.org/get", proxies=proxies)
# print(response.text)

# 2. 使用socket代理
# proxy = '127.0.0.1:7078'
# proxies = {
#     'http': 'socks5://' + proxy,
#     'https': 'socks5://' + proxy,
# }
#
# response = requests.get("http://httpbin.org/get", proxies=proxies)
# print(response.text)

# 3. 另一种使用socket代理方法
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7078)
socket.socket = socks.socksocket

response = requests.get('http://httpbin.org/get')
print(response.text)
