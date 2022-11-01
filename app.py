from flask import Flask, jsonify, render_template, redirect
from requests import get
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
# 보안 이슈

db = client.dblod


@ app.route('/')
def home():
    return render_template('index.html')


@ app.route('/visit/<int:id>', methods=["GET"])
def comment(id):
    status = ""
    data = list(db.visited.find({'member_id': id}, {'_id': False}))
    code = get(f"/visit/{id}").status_code
    # print(data)
    if code >= 500:
        status = "5xx / server error"
    elif code >= 400:
        status = "4xx / client error"
    elif code >= 300:
        status = "3xx / redirection"
    elif code >= 200:
        status = "2xx / successful"
    elif code >= 100:
        status = "1xx / informational response"

    return jsonify({'status': status, 'data': data})

@ app.route('/home')
def back():
    return redirect("/")


if __name__ == '__main__':
    app.run('0.0.0.0', port=10000, debug=True)
