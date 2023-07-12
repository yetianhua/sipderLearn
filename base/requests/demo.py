import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
r = requests.get('https://www.maoyan.com/board/4', headers)
html = etree.HTML(r.text, etree.HTMLParser())
result = html.xpath('//p[@class=name]')
print(result)