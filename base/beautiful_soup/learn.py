import lxml
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse’s story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse’s story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="linkl"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>  and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
and they lived at the bottom of a well.</p>
</body>
"""

soup = BeautifulSoup(html, 'lxml')
# 1. 基本用法
# html格式化
print(soup.prettify())
# 输出 HTML title 节点的文本内容
print(soup.title.string)

# 2. 选择元素
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 3. 提取信息
# 获取名称 可以利用 name 属性获取节点的名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 获取内容
print(soup.p.string)

# 4. 嵌套选择
