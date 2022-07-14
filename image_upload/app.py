from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://soiyo:0000@cluster0.6ufl7.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.people


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/posting', methods=['POST'])
def posting():

    title_receive = request.form["title_give"]
    content_receive = request.form["content_give"]

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'title': title_receive,
        'content': content_receive,
        'file': f'{filename}.{extension}',
    }
    db.animalCrossing.insert_one(doc)

    return jsonify({'msg': '업로드 완료!'})


@app.route('/listing', methods=['GET'])
def listing():
    articles = list(db.animalCrossing.find({}, {'_id': False}))
    return jsonify({'articles': articles})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
