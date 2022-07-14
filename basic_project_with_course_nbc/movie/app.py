# 구현 기능 : 주문(name, address, size 서버가 저장)_post, 주문목록보여주기_get(로딩완료되자마자요청)
# post_기록하기 : url, 별점, 코멘트 기록 (url 이용해서 제목, description 크롤링해 같이 DB에 넣기 : meta태그 이용)
# get_붙여주기 : 카드 붙여주기
# 서버 -> html 순으로 제작
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('클러스터 url')
db = client.people

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    cmt_receive = request.form['cmt_give']
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers) #url 입력란에서 받아옴(url_receive)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content'] #meta의 property가 og:title인 애를 가져와라
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    
    doc = {
        'title':title,
        'image':image,
        'desc':desc,
        'star':star_receive,
        'comment':cmt_receive,
    }
    db.movieLog.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movieLog.find({},{'_id':False})) #db.movieLog DB에 들어있는 데이터 모두 가져오기
    return jsonify({'movies':movie_list}) #movies라는 키 값으로 위에서 받아온 데이터 html로 넘겨줌

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)