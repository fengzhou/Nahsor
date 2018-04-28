# -*- conding:utf-8 -*-
__author__ = "Jin"
from flask import jsonify, request
from app import bp
from app.utils import dbfucs
from app.core import collect
from app.utils.log import Logger

@bp.route("/addtcass", methods=["POST"])
def addtcass():
    dictdata = request.get_json()
    testname = dictdata["testname"]
    testtype = dictdata["testtype"]
    requests = dictdata["request"]
    validate = dictdata["validate"]
    extract = dictdata["extract"]
    sql = "insert into t_testcass values(null,'%s','%s','%s','%s','%s',null,null,null);" % (testname,testtype,requests,validate,extract)
    response = {}
    data = dbfucs.excute(sql)
    if data is True:
        response["code"] = 200
        response["msg"] = data
    else:
        response["code"] = 500
        response["msg"] = data
    return jsonify(response)


@bp.route("/querytcass",methods=["POST"])
def querytcass():
    dictdata = request.get_json()
    idlist = dictdata["idlist"]
    sql = "select testname,testtype,request,validate,extract from t_testcass where id in(%s);" % idlist
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
    sql = "select testname,testtype,request,validate,extract from t_testcass where id in(%s);" % idlist
    res = dbfucs.query(sql)
    jsoncasss = []
    for test in res:
        jsoncasss.append(test)
    # print(jsoncasss)
    for i in collect.collect_db_cass(jsoncasss):
        Logger().info("*" * 90)
    Logger().info("共计[%d]条测试用例执行完成！" % len(jsoncasss))
    Logger().info("*" * 90)
    response = {}
    response["code"] = 200
    response["msg"] = "成功！！！"
    return jsonify(response)

