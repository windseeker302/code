import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
url = 'https://www.henetc.edu.cn/'
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
# page_text = response.encoding='utf-8'
print(response.text)

# with open('./henanjingmao.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)
# print('爬取数据结束！')