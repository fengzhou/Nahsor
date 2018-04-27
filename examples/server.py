# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/test', methods=['POST', 'GET'])
def test():
    dict1 = request.get_json()
    response = jsonify(dict1)
    return response

@app.route('/login', methods=['POST'])
def login():
    dict1 = request.get_json()
    username = dict1["username"]
    password = dict1["password"]
    if username == "admin" and password == "123456":
        response = {}
        response["code"] = 200
        response["msg"] = "登陆成功"
        response["data"] = "sjdh34gsalked23nlsakn45dudaj"
    else:
        response = {}
        response["code"] = 200
        response["msg"] = "登陆失败"
    response = jsonify(response)
    return response

@app.route('/chicktoken', methods=['POST', 'GET'])
def chicktoken():
    dict1 = request.get_json()
    token = dict1["token"]
    if token == "sjdh34gsalked23nlsakn45dudaj":
        response = {}
        response["code"] = 200
        response["msg"] = "操作成功"
    else:
        response = {}
        response["code"] = 200
        response["msg"] = "操作失败"
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333, debug=True)
