# -*- conding:utf-8 -*-
'''
模块管理的相关接口
'''
__author__ = "Jin"
from flask import jsonify, request
from app import bp
from app.utils import dbfucs
from app.core import collect
from app.utils.log import Logger
Logger = Logger()


@bp.route("/getmodules",methods=["GET"])
def getmodules():
    '''
    读取模块列表，这个接口是给新增用例等东西的时候，选择所属项目用的
    '''
    sql = "SELECT\
        t_product.id as productid,\
        t_product.product,\
        t_project.id as projectid,\
        t_project.project,\
        t_modules.id as moduleid,\
        t_modules.modules\
    FROM\
        t_product\
    LEFT JOIN t_project ON t_product.id = t_project.productid\
    LEFT JOIN t_modules ON t_project.id = t_modules.projectid"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/addtcass", methods=["POST"])
def addtcass():
    '''
    新增用例
    '''
    dictdata = request.get_json()
    moduleid = dictdata["moduleid"]
    testname = dictdata["testname"]
    testtype = dictdata["testtype"]
    requests = dictdata["request"]
    validate = dictdata["validate"]
    extract = dictdata["extract"]
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "insert into t_testcass values(null,'%s','%s',%s','%s','%s','%s','%s','%s',null,null);" % (moduleid,testname,testtype,requests,validate,extract,leader,remark)
    response = {}
    data = dbfucs.excute(sql)
    if data is True:
        response["code"] = 200
        response["msg"] = data
    else:
        response["code"] = 500
        response["msg"] = data
    return jsonify(response)


@bp.route("/querytcass",methods=["GET"])
def querytcass():
    '''
    获取用例列表
    编号	名称	所属模块	描述	执行状态	责任人	备注	创建时间
    '''
    sql = "SELECT\
        t_testcass.id as testid,\
        (SELECT modules FROM t_modules WHERE id = t_testcass.moduleid) as modulename,\
        t_testcass.testname,\
        t_testcass.`explain`,\
        t_testcass.status,\
        t_testcass.leader,\
        t_testcass.remark,\
        t_testcass.createtime\
    FROM\
        t_testcass\
    LEFT JOIN t_modules ON t_testcass.moduleid = t_modules.id"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/deletecass",methods=["POST"])
def deletecass():
    '''
    删除testcass
    {"pid":1}
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    sql = "DELETE FROM `t_testcass` WHERE (`id`='%s')" % pid
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "删除成功！！！"
    return jsonify(response)



@bp.route("/readcass",methods=["POST"])
def readcass():
    '''
    读取用例信息
    {"pid":1}
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    sql = "SELECT\
        moduleid,\
        testname,\
        testtype,\
        `explain`,\
        request,\
        validate,\
        extract,\
        leader,\
        remark\
    FROM t_testcass WHERE id = %s;" % pid
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/updatacass",methods=["POST"])
def updatacass():
    '''
    更新用例信息
    {
        "pid":2,
        "product":"产品名称",
        "explain":"描述",
        "leader":"责任人",
        "remark":"备注"
    }
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    moduleid = dictdata["moduleid"]
    testname = dictdata["testname"]
    testtype = dictdata["testtype"]
    requests = dictdata["request"]
    validate = dictdata["validate"]
    extract = dictdata["extract"]
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "UPDATE `t_testcass`\
        SET `moduleid` = '%s',\
        `moduleid` = '%s',\
        `testname` = '%s',\
        `testtype` = '%s'\
        `request` = '%s'\
        `validate` = '%s'\
        `extract` = '%s'\
        `leader` = '%s'\
        `remark` = '%s'\
        WHERE (`id` = '%s')" % (moduleid,testname,testtype,requests,validate,extract,leader,remark,pid)
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "更新成功！！！"
    return jsonify(response)




@bp.route("/runtests", methods=["POST"])
def runtests():
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
