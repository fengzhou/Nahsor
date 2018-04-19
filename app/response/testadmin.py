import pytest
import subprocess

@app.route('/run')
def run():
    args = ['--alluredir=./result']
    pytest.main(args)
    allure = subprocess.Popen('allure generate ./result/ -o ./static/report/ --clean', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print()
    response = {}
    response["code"] = 200
    response["msg"] = "%s" % allure.stdout.read()
    return jsonify(response)