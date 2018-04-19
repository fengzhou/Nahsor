# -*- conding:utf-8 -*-
__author__ = "Jin"
from flask import jsonify
from app import bp
import pytest
import subprocess


@bp.route("/run", methods=["get"])
def run():
    args = ['--alluredir=./result']
    pytest.main(args)
    allure = subprocess.Popen('allure generate ./result/ -o ./static/report/ --clean', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print()
    response = {}
    response["code"] = 200
    response["msg"] = "%s" % allure.stdout.read()
    return jsonify(response)

bp.route("/test")
def test():
    return "helo"