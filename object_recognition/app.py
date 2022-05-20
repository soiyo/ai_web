from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient(
    '클러스터URL')
db = client.wordfiles


@app.route('/')
def main():
    msg = request.args.get("msg")

    # DB에서 저장된 단어 찾아서 HTML에 나타내기
    words = list(db.words.find({}, {"_id": False}))
    return render_template("index.html", words=words, msg=msg)


@app.route('/detail/<keyword>')
def detail(keyword):
    # API에서 단어 뜻 찾아서 결과 보내기
    status_receive = request.args.get("status_give", "old")
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}",
                     headers={"Authorization": "Token d73ee353c661cf2242d2a8ea8a8841a28b44deaf"})
    if r.status_code != 200:
        return redirect(url_for("main", msg="Word not found in dictionary; Try another word"))
    result = r.json()
    print(result)
    return render_template("detail.html", word=keyword, result=result, status=status_receive)


@app.route('/api/save_word', methods=['POST'])
def save_word():
    # 단어 저장하기
    word_receive = request.form['word_give']
    definition_receive = request.form['definition_give']
    doc = {"word": word_receive, "definition": definition_receive}
    db.words.insert_one(doc)
    return jsonify({'result': 'success', 'msg': f'word "{word_receive}" saved'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    # 단어 삭제하기
    word_receive = request.form['word_give']
    db.words.delete_one({"word": word_receive})
    db.examples.delete_many({"word": word_receive})
    return jsonify({'result': 'success', 'msg': f'word "{word_receive}" deleted'})


@app.route('/api/get_examples', methods=['GET'])
def get_exs():
    word_receive = request.args.get("word_give")
    result = list(db.examples.find({"word": word_receive}, {'_id': 0}))
    print(word_receive, len(result))

    return jsonify({'result': 'success', 'examples': result})


@app.route('/api/save_ex', methods=['POST'])
def save_ex():
    word_receive = request.form['word_give']
    example_receive = request.form['example_give']
    doc = {"word": word_receive, "example": example_receive}
    db.examples.insert_one(doc)
    return jsonify({'result': 'success', 'msg': f'example "{example_receive}" saved'})


@app.route('/api/delete_ex', methods=['POST'])
def delete_ex():
    word_receive = request.form['word_give']
    number_receive = int(request.form["number_give"])
    example = list(db.examples.find({"word": word_receive}))[
        number_receive]["example"]
    print(word_receive, example)
    db.examples.delete_one({"word": word_receive, "example": example})
    return jsonify({'result': 'success', 'msg': f'example #{number_receive} of "{word_receive}" deleted'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
