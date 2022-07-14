from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/detail')
def detail():
    word_receive = request.args.get("word_give")
    return render_template("detail.html", word=word_receive)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
