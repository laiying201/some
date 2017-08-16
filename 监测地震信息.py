import requests
from bs4 import BeautifulSoup

user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
headers = {'User-Agent':user_agent}
url = 'http://www.ceic.ac.cn/speedsearch'
session = requests.Session()

try:
    request = session.get(url,headers=headers)
    html = request.text
    # print(html)
    # with open('earthquake.html','rb') as f:
    #   html = f.read()
    soup = BeautifulSoup(html,"html.parser")
    title_ls = soup.find_all('th')
    titles = [x.get_text() for x in title_ls]
    # print(titles)
    tr_ls = soup.find_all('tr')
    if len(tr_ls) > 0:
        for tr in tr_ls:
            td_info = [td.get_text() for td in tr.find_all('td')]
            if len(td_info) > 0:
                quake_info = dict(zip(titles,td_info))
                print(quake_info)
    else:
        print('No earthquake info')
except :
    print('Something wrong!try again')


