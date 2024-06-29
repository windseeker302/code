import requests
url = 'https://www.henetc.edu.cn/__local/0/2D/28/A5B1CBC7B5F9265BCD2A00784F1_3CD94549_1C769.jpg?e=.jpg'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

img_data = requests.get(url,headers=headers).content
with open('./img.jpg','wb') as fp:
    fp.write(img_data)