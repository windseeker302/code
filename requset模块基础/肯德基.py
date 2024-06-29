import requests
import json

def Kfc():
    city =  '中山'  #input('请输入城市名称：')
    params = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': '2',
        'pageSize': '10'
    }


    response = requests.post(url,params=params,headers=headers)
    list_content = response.json()
    data = list_content['Table1']
    for i in data:
        print(i)


if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}   
    Kfc()
    


# import requests
# import json

# def Kfc():
#     keyword = input("请输入城市名称：")
#     for i in range(1, 11):
#         pms = {
#             'cname': '',
#             'pid': '',
#             'keyword': keyword,
#             'pageIndex': i,
#             'pageSize': '10'
#         }
#         res = requests.post(url=url, data=pms, headers=headers)
#         data = res.json()
#         xdata = data["Table1"]   # 获取详情数据
#         for i in xdata:
#             print(i)

# if __name__ == '__main__':
#     url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
#     }
#     Kfc()