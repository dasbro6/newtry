import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def retrieve_vollydata_list(url):
    r = requests.get(url,headers)
    pattern = re.compile('">(.*?)<\/a><\/figcaption>\s+<\/figure>\s+<\/td>\s+<td><\/td>\s+<td class="text--number group--start">(.*?)<\/td>\s+<td class="text--number result--highlight text--highlight">(.*?)<\/td>\s+<td class="text--number group--end">(.*?)<\/td>')
    p = re.findall(pattern, r.text)
    return p

vl_url ='https://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
result = retrieve_vollydata_list(vl_url)
print(result)
