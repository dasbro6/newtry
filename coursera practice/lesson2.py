#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',}

response = requests.get('https://book.douban.com/subject/26163553/comments/'+ str(i+1), headers=headers)
print(response.status_code)
print(response.headers['content-type'])
# # 'application/json; charset=utf8'
response.encoding
# # 'utf-8'


# re = requests.get('http://money.cnn.com/data/dow30/')     # the url may change print(re.text)
# print(re.text)
# markup = '<p class="title"><b>The Little Prince</b></p>'
# soup = BeautifulSoup(markup,"lxml")
# print(type(soup.b))
# tag = soup.p
# print(tag.string)

soup =BeautifulSoup(response.text,'lxml')
pattern = soup.find_all('span','short')
for item in pattern:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*) rating" title="力荐"></span>')
p = re.findall(pattern_s,response.text)
print(len(p))

# s = 0
# count = 0
# p_list=p[0,50]
# for star in p:
#     s += int(star)
#     if star>0:
#         count += 1
# print(s)

