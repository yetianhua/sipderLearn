import socket
import urllib.request
from urllib.request import ProxyHandler, build_opener

import socks

# 1. 设置http代理
# proxy = '127.0.0.1:7078'
#
# proxy_handler = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'http://' + proxy,
# })
#
# opener = build_opener(proxy_handler)
#
# response = opener.open('http://httpbin.org/get')
# print(response.read().decode('utf-8'))


# 2. 设置socket代理
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7078)
# socket.socket = socks.socksocket
#
# response = urllib.request.urlopen('http://httpbin.org/get')
# print(response.read().decode('utf-8'))
