from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient(
    '클러스터URL')
db = client.people


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/diary', methods=['GET'])
def show_diary():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET 연결 완료!'})


@app.route('/diary', methods=['POST'])
def save_diary():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST 요청 완료!'})


@app.route('/posting', methods=['POST'])
def posting():
    title_receive = request.form["title_give"]
    content_receive = request.form["content_give"]

    doc = {
        'title': title_receive,
        'content': content_receive
    }
    db.articles.insert_one(doc)

    return jsonify({'msg': '업로드 완료!'})


@app.route('/listing', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id': False}))
    return jsonify({'articles': articles})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
