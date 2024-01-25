import requests as req
from bs4 import BeautifulSoup as bs
web = req.get('https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202#childTab_tmp')
soup = bs(web.content, 'html5lib')
date = soup.select('.menu-tbl .date')
day = soup.select('.menu-tbl .day')
won = soup.select('h3.menu-tit01')
menu = soup.select('h3.menu-tit01+p')

def Busunv():
    for y,d,w,m in zip(date,day,won,menu):
        print('-'*15)
        print(f'{y.text} ({d.text})')
        print('-'*15)
        print(w.text)
        print(m.text)



if __name__ == '__main__':
    Busunv()

    
# print(__name__)