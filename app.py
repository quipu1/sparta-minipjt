from flask import Flask, jsonify, render_template, redirect, request
from requests import get
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("키값은 따로 입력해주셔야 해요! 제 DB 쓰신다면 링크 슬랙에 넣어두겠습니다.")


db = client.dblod

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/visit/<member_id>", methods=["GET"])
def comment(member_id):
    status = ""
    data = list(db.visited.find({'member_id': int(member_id)}, {'_id': False}))
    if data is not "":
        status = "200 / successful"
    else:
        status = "error response"

    return jsonify({'status': status, 'data': data})


@app.route("/visit/add/<member_id>", methods=["POST"])
def visited_post(member_id):
    visited_id_receive = request.form['visited_id_give']
    visited_comment_receive = request.form['visited_comment_give']
    doc = {
        'id': visited_id_receive,
        'comment': visited_comment_receive,
        'member_id': int(member_id)
    }
    db.visited.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route('/home')
def back():
    return redirect("/")


if __name__ == '__main__':
    app.run('0.0.0.0', port=10000, debug=True)
