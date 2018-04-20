# -*- conding:utf-8 -*-
__author__ = "Jin"
from flask import jsonify, request
from app import bp
from app.utils import dbfucs
import pytest
import subprocess


@bp.route("/run", methods=["GET"])
def run():
    # args = ['--alluredir=./result']
    # pytest.main(args)
    allure = subprocess.Popen('allure generate ./result/ -o ./static/report/ --clean', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print()
    response = {}
    response["code"] = 200
    response["msg"] = "%s" % allure.stdout.read()
    return jsonify(response)


@bp.route("/addtcass", methods=["POST"])
def addtcass():
    sql = "insert into t_testcass values(null,'tastcass','{\"\key\":\"values\"}','2333',null,null)"
    response = {}
    response["code"] = 200
    response["msg"] = dbfucs.excute(sql)
    return jsonify(response)


@bp.route("/querytcass",methods=["POST"])
def querytcass():
    dictdata = request.get_json()
    idlist = dictdata["idlist"]
    sql = "select cassname,testcass from t_testcass where id in(%s);" % idlist
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)

