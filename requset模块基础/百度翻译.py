import requests
import json
url = 'https://fanyi.baidu.com/sug'

ws = input('enter a word:')
data = {
    'kw': ws
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.post(url,headers=headers,data=data)  

dict_obj = response.json()

ws += '翻译.json'
fp = open(ws,'w',encoding='utf-8')
json.dump(dict_obj,fp=fp,ensure_ascii=False)

# ws += '翻译.json'
# with open(ws,'w',encoding='utf-8') as ws:
#    ws.write(str(respones.json()))
print("翻译over")