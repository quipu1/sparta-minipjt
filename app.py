from flask import Flask, jsonify, render_template, redirect, request
from requests import get
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://test:test@cluster0.lrizo6r.mongodb.net/?retryWrites=true&w=majority')


db = client.dblod

@app.route("/")
def home():
    return render_template('member.html')


@app.route("/<member_id>", methods=["GET"])
def rrrr(member_id):
    doc = {
        "_id":{"$oid":"6360bc044a3572efd80ebf04"},
        "name":"최승호",
        "mbti":"ENTP",
        "desc":"축구와 게임을 좋아합니다. 화성에 지내고 있고, 전자공학을 전공했습니다. 졸업 후에 회사를 몇군데 다녀보다 개발자에 도전하게 되었습니다.모자란 게 많으니 많이 도와주세요. 잘부탁드려요",
        "stpoint":"부정적인 일들을 금세 잊고 털어버립니다.",
        "style":"대화를 통해 생각을 교류하며 수정해 나가는 스타일 입니다.",
        "blog":"https://akrt.tistory.com",
        "member_id": member_id
        }
    
    return jsonify({'data':doc})

@app.route("/visit/<member_id>", methods=["GET"])
def comment(member_id):
    status = ""
    data = list(db.visited.find({'member_id': member_id}, {'_id': False}))
    if data != "":
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
