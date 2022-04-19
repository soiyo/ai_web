#로컬 개발환경 셋팅
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/') #기본창구
def home():
   return render_template('index.html') #html파일을 띄워준다

#get 요청 
@app.route('/testGet', methods=['GET']) #testGet창구
def test_get():
    title_receive = request.args.get('title_give') #title_give를 받아와서 print해줌
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'}) #index.html에 response로 전달

@app.route('/testPost', methods=['POST']) #testPost창구
def test_post():
    title_receive = request.form['title_give'] #title_give를 받아와서 print해줌
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'}) #print 후 데이터 돌려줌 -> response에 이 값 들어감


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)