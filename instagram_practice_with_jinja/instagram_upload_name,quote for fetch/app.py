from datetime import datetime
import os
from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://soiyo:0000@cluster0.6ufl7.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta_plus_week4


@app.route('/')
def home():
    return render_template("first.html")


@app.route('/simpsonlist')
def simpsonslist():
    thisdb = list(db.user.find({}, {'_id': False}))
    # html 에서 simpsons라는 변수 사용
    return render_template(("index.html"), simpsons=thisdb)


@app.route('/getsimpson')
def get():
    thisdb = list(db.user.find({}, {'_id': False}))
    # html 에서 simpsons라는 변수 사용
    return jsonify({'intro': thisdb})


@app.route('/postsimpson', methods=['POST'])
def posting():
    name_receive = request.form['name_give']
    quote_receive = request.form['quote_give']
    picture_receive = request.files['picture_give']

    doc = {'name': name_receive, 'quote': quote_receive,
           'picture': picture_receive}
    db.user.insert_one(doc)
    # html 에서 simpsons라는 변수 사용
    return jsonify({'msg': '업로드 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
