# 如果请求中需要加入Headers等信息，就可以利用更强大的Request 类来构建。
import urllib.request
import urllib.parse
# 1. 简单使用Request
# request = urllib.request.Request('https://www.python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 2. Request 参数介绍 Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个参数url用于请求URL，这是必传参数
# 第二个参数 data 如果要传，必须传 bytes （字节流）类型的
# 第三个参数 headers 是一个字典，它就是请求头，我们可以在构造请求时通过 headers 参数直接构造，也可以通过调用请求实例的 add_header（）方法添加。
# 第四个参数 origin_req_host 指的是请求方的 host 名称或者 IP地址。
# 第五个参数unveri干iable 表示这个请求是否是无法验证的，默认是False，意思就是说用户没 有足够权限来选择接收这个请求的结果。例如，我们请求一个 HTML 文档中的图片，但是我 们没有向动抓取图像的权限，这时 unverifiable 的值就是True。
# 第六个参数 method 是一个字符串 ，用来指示请求使用的方法，比如 GET、POST和 PUT 等。

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Host': 'httpbin.org'
}
data = bytes(urllib.parse.urlencode({'name': 'Germey'}), encoding='utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# 另外，headers也可以用 add_header（）方法来添加：request.set_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# 3. 高级用法 我们虽然可以构造请求，但是对于一些更高级的操作（比如 Cookies 处理、代 理设置等），我们该怎么办呢？
# 高级用法一般都是使用Hander构建opener，opener.open()和request.urlopen()是一样的

# 4.
