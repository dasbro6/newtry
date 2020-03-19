from bs4 import BeautifulSoup
import requests
import re

r = requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.7310346603232132&callback=jQuery1112011767468561233518_1583765649093&_=1583765649098')
rcode = r.status_code
print(rcode)




rtext = r.text.encode('utf-8').decode('unicode-escape')
print(rtext)
soup =BeautifulSoup(rtext,'lxml')

pattern_s = re.compile(',"title":"(.*?)"')
p = re.findall(pattern_s,rtext)
s = 0
for star in p:
    print(star)
