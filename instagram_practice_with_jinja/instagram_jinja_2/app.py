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


@app.route('/feed')
def feed():
    return render_template("index.html")


@app.route('/user')
def userpage():
    user_id = request.args.get('id')  # 1010 할당
    user_info = db.user.find_one({"id": user_id})
    return render_template("user.html", info=user_info)  # info를 html에 넘겨줌


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
