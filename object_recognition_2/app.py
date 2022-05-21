from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/wiki')
def wiki():
    return render_template("wiki.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
