import logging

import requests

# 1. 基本用法
# r = requests.get('http://www.baidu.com/')
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# 2. Get请求
# 2.1 get请求使用参数
# 方法1
# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# 方法2
# r = requests.get('http://httpbin.org/get', params={'name': 'germey', 'age': 22})
# print(r.text)

# 2.2 返回结构 如果返回类型实际上是str类型，而且是JSON结构，则可以调用json方法
# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# 2.3 抓取网页
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, r.text)
# print(title)

# 2.4 抓取二进制数据
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# 3. POST请求
# r = requests.post('http://httpbin.org/post', data={'name':'germey','age':'22'})
# print(r.text)

# 4. 响应 （响应的一些属性）
# r = requests.get('http://www.jianshan.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
#
# # 4.1 状态码
# if not r.status_code == requests.codes.ok:
#     print('not success')

# 5. 高级用法
# 5.1 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 5.2 cookies
# 简单使用cookies
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# header使用cookies
# headers = {
#     'Cookie': '_9755xjdesxxd_=32; YD00517437729195:WM_TID=q/90Qz+b6wFFVFFQARZrtMIDtfaDeGw0; __utma=155987696.146243863.1590371373.1646113133.1646113133.1; _zap=1851a723-481a-4069-adf0-af2b2d6826cf; q_c1=f66dd3e2a2b142918b4d357a8b1149de|1660724572000|1590787030000; _xsrf=tblQc5GaPOk8HJHllbFGl5cCbwpPaUl5; YD00517437729195:WM_NI=ZgxKZEMuihyDwG3qmt+T9EuEtdD0LoDGx/DdY4ytAMGcdGHY1f+VU6gMwEmZo5KN6lsPijSzqK4vlXX8wYB59qnr5ewnDXL9UE3uduwzCVeD7YKmCN5A0+X9jshHWIGrTWI=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eebbc73993f1b9bbcd3988ac8ea3d44b968e8e86c15cf3b6a9b0e633fb879caed32af0fea7c3b92a9ab9b8acd94f8faba789fc50b599fd92f080e98cf7a6f84fb8bc8cd1cf658899b8d0c7709becb795c44785bdaca8cb53f3bae5b7d83ea593b9a6f052adeb85afb568b190a78bd272b395fc97ef549ce8b9bac13ffbafa293b86fb5b28cb9cf33979bfd96e77fb5a68db7e850f587858ec246f79f00ccdb33aaada8a9d64385ae9cb8cc37e2a3; d_c0=ALAYCDBB1BaPTkk8iPd7Igv99fVqEesxex4=|1684981289; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1686223485,1686879320; SL_G_WPT_TO=zh; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; z_c0=2|1:0|10:1687921506|4:z_c0|80:MS4xYkloNUFBQUFBQUFtQUFBQVlBSlZUYmlqaG1YYkRPMnB5b1BSdlJBLXEtRGZPS0I5N0xZWlVBPT0=|f4ce2798e3808e16ceea5e82ee40f25424ab1e2b54de6c52cbd1e7caec877b4d; SESSIONID=ZB1bM5AcQ1U1sNm3NgICeAbmCQa54cp5W4GIcUKnoYl; JOID=U1ATCkMhc3VJNQ7LbymDovPSm0d5cj9LKnEyhAN5Sy53R0mvUvG53CU1CcphIKsok7mwBPS_54rqwfqkFNF_cEw=; osd=W1wQC0Mpf3ZINQbHbCiDqv_RmkdxfjxKKnk-hwJ5QyJ0RkmnXvK43C05CsthKKcrkrm4CPe-54LmwvukHN18cUw=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1688718321; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1688718320|1688707328',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# 通过cokiesjar使用cookies
# from requests.cookies import RequestsCookieJar
#
# cookies = '_9755xjdesxxd_=32; YD00517437729195:WM_TID=q/90Qz+b6wFFVFFQARZrtMIDtfaDeGw0; __utma=155987696.146243863.1590371373.1646113133.1646113133.1; _zap=1851a723-481a-4069-adf0-af2b2d6826cf; q_c1=f66dd3e2a2b142918b4d357a8b1149de|1660724572000|1590787030000; _xsrf=tblQc5GaPOk8HJHllbFGl5cCbwpPaUl5; YD00517437729195:WM_NI=ZgxKZEMuihyDwG3qmt+T9EuEtdD0LoDGx/DdY4ytAMGcdGHY1f+VU6gMwEmZo5KN6lsPijSzqK4vlXX8wYB59qnr5ewnDXL9UE3uduwzCVeD7YKmCN5A0+X9jshHWIGrTWI=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eebbc73993f1b9bbcd3988ac8ea3d44b968e8e86c15cf3b6a9b0e633fb879caed32af0fea7c3b92a9ab9b8acd94f8faba789fc50b599fd92f080e98cf7a6f84fb8bc8cd1cf658899b8d0c7709becb795c44785bdaca8cb53f3bae5b7d83ea593b9a6f052adeb85afb568b190a78bd272b395fc97ef549ce8b9bac13ffbafa293b86fb5b28cb9cf33979bfd96e77fb5a68db7e850f587858ec246f79f00ccdb33aaada8a9d64385ae9cb8cc37e2a3; d_c0=ALAYCDBB1BaPTkk8iPd7Igv99fVqEesxex4=|1684981289; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1686223485,1686879320; SL_G_WPT_TO=zh; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; z_c0=2|1:0|10:1687921506|4:z_c0|80:MS4xYkloNUFBQUFBQUFtQUFBQVlBSlZUYmlqaG1YYkRPMnB5b1BSdlJBLXEtRGZPS0I5N0xZWlVBPT0=|f4ce2798e3808e16ceea5e82ee40f25424ab1e2b54de6c52cbd1e7caec877b4d; SESSIONID=ZB1bM5AcQ1U1sNm3NgICeAbmCQa54cp5W4GIcUKnoYl; JOID=U1ATCkMhc3VJNQ7LbymDovPSm0d5cj9LKnEyhAN5Sy53R0mvUvG53CU1CcphIKsok7mwBPS_54rqwfqkFNF_cEw=; osd=W1wQC0Mpf3ZINQbHbCiDqv_RmkdxfjxKKnk-hwJ5QyJ0RkmnXvK43C05CsthKKcrkrm4CPe-54LmwvukHN18cUw=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1688718321; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1688718320|1688707328'
# jar = RequestsCookieJar()
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=', 1)
#     jar.set(key, value)
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com', headers=headers, cookies=jar)
# print(r.text)

# 5.3 会话维持
# 在requests 中，如果直接利用get （）或 post （）等方法的确可以做到模拟网页的请求，但是这实际 上是相当于不同的会话，也就是说相当于你用了两个浏览器打开了不同的页面。
# 其实解决这个 问题的 主要方法就是维持同 一个会话，也就是相当于打开一个新的浏览器选项 卡而不是新开一个浏览器。但是我又不想每次设置 cook ies ，那该怎么办呢 ？这时候就有了 新的 利器一－ Session 对象。
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 5.4 SSL证书验证
# requests还提供了证书验证的功能。当发送 HTTP 请求的时候，它会检查 SSL证书，我们 可以使用verify参数控制是否检查此证书。其实如果不加 verify 参数的话，默认是True ，会自动验证。
# # import urllib3
# urllib3.disable_warnings() # 设置忽略告警方式屏蔽警告

# logging.captureWarnings(True) # 通过捕获告警到日志方式忽略告警
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.status_code)

# 我们也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或 一个包含两个文件路径的元组：
# r = requests.get('https://www.12306.cn', cert=('/path/server.crt','/path/key'))
# print(r.status_code)

# 5.5 代理设置
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'https://10.10.1.10:1080'
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# 代理使用BasicAuth
# proxies = {
#     'http': 'http://user:password@10.10.1.10:3128',
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# requests支持SOCKS协议的代理
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# 5.6 超时
# 超时时间设置为1秒，如果1秒内没有响应，那就抛出异常
# requests.get('https://www.taobao.com', timeout=1)
# 请求分为两个阶段，即连接（ connect ）和读取（ read ） , 如果要分别指定，就可以传入一个元组
# requests.get('https://www.taobao.com', timeout=(5, 11, 30))

# 5.7 身份认证
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# 5.8 Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
s = requests.Session()
req = requests.Request('POST', url, data=data, headers=headers)
prepare = s.prepare_request(req)
r = s.send(prepare)
print(r.text)