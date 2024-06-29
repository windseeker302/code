import requests
import json

url = 'https://answers.henetc.edu.cn/answers/core/mobile/paper/getErrorQuestionsListAjax'

data = {
    'idnum': '23070310108',
    'report_number': 'F4551E6E4029B832',
    'aid': 'answers',
    'pid': 'yyzx',
    'token': 'eed96d7c4b0b7053cd69b057c547aa94'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
res = requests.post(url,params=data,headers=headers)
xdata = res.text
json_str = json.loads(xdata)
# data 内容
zong = json_str["data"]
# 获取 1-100 题正确的选项
for i in range(0,100):
    right_option = zong[i]['options']
    timu = zong[i]['questions']
    for x in timu:
        timu = (x['content'])
    for j in right_option:
        if j['is_right'] == '1':
            klawjd = '这是第'+ str(i) + "题" + '题目是' + str(timu) + "正确选项是" + j['content']
            with open('./100题答案','a',encoding='utf-8')as ws:
                ws.write(str(klawjd))
                ws.write('\n')




# import requests
# url = 'https://answers.henetc.edu.cn/answers/core/mobile/paper/getErrorQuestionsListAjax'
# #f12请求
# payload = {
# 	"idnum": "23070310108",
# 	"report_number": "F4551E6E4029B832",
# 	"aid": "answers",
# 	"pid": "yyzx",
# 	"token": "eed96d7c4b0b7053cd69b057c547aa94"
# }
# header={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# }
# res = requests.post(url,data=payload, headers=header)
# res.encoding = res.apparent_encoding
# with open('result_new.txt', mode='a', encoding='utf-8') as writer:
#     for _ in res.json()['data']:
#         wenti = _['questions'][0]['content']
#         writer.write(f'Q:{wenti}\n')
#         for xuanxiang_json in _['options']:
#             if xuanxiang_json['is_right'] == '1':
#                 daan = xuanxiang_json['content']
#                 writer.write(f'A:{daan}\n')
#         writer.write('\n')

 