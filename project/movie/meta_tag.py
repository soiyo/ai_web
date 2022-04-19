#프로젝트 만들기 전 : 메타 태그 조각기능 사용해보기
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('meta[property="og:title"]')['content'] #meta의 property가 og:title인 애를 가져와라
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
print(title,image,desc)