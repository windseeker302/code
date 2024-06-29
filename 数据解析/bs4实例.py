from bs4 import BeautifulSoup
import requests

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
page_text = requests.get(url,headers=headers).text
soup = BeautifulSoup(page_text,'lxml')
a_list = soup.select('.book-mulu > ul > li')
fp = open('./三国.txt','w',encoding='utf-8')
for i in a_list:
    herf = 'https://www.shicimingju.com/' + i.a['href']
    title = i.a.string
    new_page_text = requests.get(herf,headers=headers).text
    new_soup = BeautifulSoup(new_page_text,'lxml')
    content = new_soup.find('div',class_='card bookmark-list').text
    fp.write(content)
    