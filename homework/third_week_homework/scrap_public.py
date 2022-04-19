#평점 하나 가져오기:가버나움
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('클러스터 url')
db = client.people
movie = db.movies.find_one({'title':'가버나움'})['star'] #평점가져오기
# print("가버나움의 평점 : "+movie)

#가버나움의 평점과 같은 영화제목들 가져오기
# for i in (0,1):
#     all_movies = list(db.movies.find({'star':movie},{'_id':False}))[i]['title']
#     print(all_movies)

#가버나움 평점 0으로 만들기 : 주의) 0은 문자열!!!
# rank_down = db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
print("가버나움의 평점 : "+movie)