# 判断网页是否可爬
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.maoyan.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.maoyan.com/board/4'))