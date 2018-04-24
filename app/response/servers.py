# -*- conding:utf-8 -*-
__author__ = "Jin"
from flask import jsonify, request
from app import bp
from app.utils import dbfucs
from app.core import jsonfuc


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

@bp.route("/testgo", methods=["POST"])
def testgo():
    dictdata = request.get_json()
    idlist = dictdata["idlist"]
    sql = "select cassname,testcass from t_testcass where id in(%s);" % idlist
    res = dbfucs.query(sql)
    jsoncasss = []
    for test in res:
        jsoncasss.append(test["testcass"])
    # print(jsoncasss)
    for i in jsonfuc.collect_db_cass(jsoncasss):
        print("用例执行结束")
    response = {}
    response["code"] = 200
    response["msg"] = "成功！！！"
    return jsonify(response)