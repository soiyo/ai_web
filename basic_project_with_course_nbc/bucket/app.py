# 구현 : 서버에 버킷리스트 전달, 버킷리스트의 번호를 서버에서 만들어주기-> 몇 번째 버킷목록을 완료했는지 컴퓨터가 알아듣게 Post로 전송, 버킷리스트 보여주기
from ast import Num
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('클러스터 url')
db = client.people

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket.find({},{'_id':False}))
    count=len(bucket_list)+1
    doc = {
        'num':count,
        'done':0,
        'bucket':bucket_receive
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets': bucket_list})

@app.route("/bucket/done", methods=["POST"])
def bucket_done(): #버킷을 완료했으면
    num_receive = request.form['num_give'] #html에서 입력num값을 받아옴 (자동생성:bucket_post(), 몇번째 버킷을 완료했는지 post로 받아오고)
    db.bucket.update_one({'num':int(num_receive)},{'$set':{'done':1}}) #(주의) 숫자를 클라이언트로 받아오면 숫자로 바꿔줘야함. (안그러면 문자로인식)/ done을 1로바꿔줌
    return jsonify({'msg': '버킷 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)