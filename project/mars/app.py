# 구현 : 주문(name, address, size 서버가 저장)_post, 주문목록보여주기_get(로딩완료되자마자요청)
from pymongo import MongoClient
client = MongoClient('cluster URL')
db = client.people

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give'] #데이터 받음
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = { #DB에 저장
        'name':name_receive,
        'address':address_receive,
        'size':size_receive,
    }
    db.mars.insert_one(doc) #하나추가요
    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({},{'_id':False})) #db.mars라는 곳에서 찾기(모든 내역, id제외)
    return jsonify({'orders': order_list}) #orders라는 키로 order_list 찾은거 내려줌

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)