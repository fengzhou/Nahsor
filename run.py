from flask import Flask, render_template, jsonify
import pytest
import subprocess
app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    return '<h1>请访问http://127.0.0.1:8808/report/index.html</h1>'


@app.route('/run')
def run():
    args = ['--alluredir=./test']
    pytest.main(args)
    allure = subprocess.Popen('allure generate ./test/ -o ./static/report/ --clean', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print()
    response = {}
    response["code"] = 200
    response["msg"] = "%s" % allure.stdout.read()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8808, debug=True)
