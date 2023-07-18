import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 猫眼添加了验证，要通过验证才可以访问url，所以需要换url
r = requests.get('https://www.maoyan.com/board/4?requestCode=270a54f2f058b4c78673e84675b66472p2fox', headers)
r.encoding = r.apparent_encoding
print(r.text)
html = etree.HTML(r.text, etree.HTMLParser())
result = html.xpath('//p[@class="name"]/a/text()')
print(result)
