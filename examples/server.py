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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2333, debug=True)
