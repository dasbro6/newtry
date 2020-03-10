#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import re
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',}

count = 0
i = 0
list_star=[]
s = 0
count_del = 0
count_s = 0
while count<50:
    try:
        response = requests.get('https://book.douban.com/subject/26163553/comments/hot?p='+ str(i+1), headers=headers)
    # print(response.status_code)
    # print(response.headers['content-type'])
    except Exception as err:
        print(err)
        break

    soup =BeautifulSoup(response.text,'lxml')
    comment = soup.find_all('span','short')
    pattern_s = re.compile('<span class="user-stars allstar(.*) rating" title="力荐"></span>')
    p = re.findall(pattern_s,response.text)
    # print(comment)
    for item in comment:
        count += 1
        if count > 50:
            count_del += 1     # count the number of comments more than 50 of the page
        else:
            print(count, item.string)
    for star in p:
        list_star.append(int(star))

    # print(len(p))
    time.sleep(5)
    i += 1
    # print(list_star)
    for star in list_star[:-count_del]:   # calculate the rating star of 50 comments
        s += int(star)
if count >= 50:
    print(count_del,count_s)
    print(s,len(list_star))
    print(s // (len(list_star)-count_del))
# s = 0
# count = 0
# p_list=p[0,50]
# for star in p:
#     s += int(star)
#     if star>0:
#         count += 1
# print(s)

