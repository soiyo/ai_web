#genie music 의 순위 제목 가수 찍기
#앞의 두 글자만 끊기는 text[0:2]
#앞에 여백 제거 strip()
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#곡이름
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis


music= soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for m in music:
    title=m.select_one('td.info > a.title.ellipsis').text
    rank=m.select_one('td.number').text[0:2]
    singer=m.select_one('td.info > a.artist.ellipsis').text
    print(rank, title.strip(), singer)
    #여백제거 .strip()
