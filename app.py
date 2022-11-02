from flask import Flask, jsonify, render_template, redirect, request
from requests import get
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://test:test@cluster0.lrizo6r.mongodb.net/?retryWrites=true&w=majority')

db = client.dblod


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/member/<member_id>")
def member(member_id):
    return render_template('member.html', member_id=member_id)


@app.route("/<member_id>", methods=["GET"])
def info_get(member_id):
    members_list = list(db.members.find({'member_id': int(member_id)}, {'_id': False}))
    return jsonify({'members': members_list})


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
