#방명록 저장하고 로딩 완료시 자동으로 붙여주는거
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('클러스터 url')
db = client.people

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    cmt_receive = request.form['comment_give']
    
    doc = {
        'name':name_receive,
        'comment':cmt_receive,
    }
    db.animalCrossing.insert_one(doc)
    return jsonify({'msg':'기록 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    homework_list = list(db.animalCrossing.find({},{'_id':False}))
    return jsonify({'homework':homework_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)