#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import re

def retrieve_djdate_list():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    r = requests.get('https://money.cnn.com/data/dow30/',headers)
    print(r.text)
    # soup = BeautifulSoup(r.text, 'lxml')
    pattern = re.compile('class="wsod_symbol">(.*?)<\/a>&nbsp;<span.*?">(.*?)<\/span><\/td>\s+.*?class="wsod_stream">(.*?)<\/span><\/td>')
    p = re.findall(pattern, r.text)

    return p

print(retrieve_djdate_list())