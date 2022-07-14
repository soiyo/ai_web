from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient(
    '클러스터URL')
db = client.dbsparta_plus_week4


@app.route('/')
def home():
    return render_template("first.html")


@app.route('/feed')
def feed():
    feeds = db.user.find()
    return render_template(("index.html"), feed=feeds)  # html 에서 feed라는 변수 사용


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
