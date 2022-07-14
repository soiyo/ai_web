from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    r = requests.get(
        'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    # api를 통해서 가져온 미세먼지 정보를 rows에다가 저장하고, 이를 index.html로 보냅니다.
    return render_template("index.html", rows=rows)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
