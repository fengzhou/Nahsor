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
from app.utils.jsonfuc import dict_to_dbjson
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
    {
        "moduleid":1,
        "testname":"测试用例名称",
        "testtype":"testcass",
        "explain":"用例描述",
        "request":{},
        "validate":[],
        "extract":[],
        "leader":"LangJin",
        "remark":"备注信息"
    }
    '''
    dictdata = request.get_json()
    moduleid = dictdata["moduleid"]
    testname = dictdata["testname"]
    testtype = dictdata["testtype"]
    explain = dictdata["explain"]
    requests = dict_to_dbjson(dictdata["request"])
    validate = dict_to_dbjson(dictdata["validate"])
    extract = dict_to_dbjson(dictdata["extract"])
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "insert into t_testcass \
    (`moduleid`, `testname`, `testtype`, `explain`, \
    `request`, `validate`, `extract`, `leader`, `remark`) \
    values('%s','%s','%s','%s','%s','%s','%s','%s','%s');\
    " % (moduleid,testname,testtype,explain,requests,validate,extract,leader,remark)
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
        (select t_reports.`status` from t_reports WHERE id = t_testcass.id order by id DESC limit 1) as `status`,\
        t_testcass.leader,\
        t_testcass.remark,\
        t_testcass.createtime\
    FROM\
        t_testcass\
    LEFT JOIN t_modules ON t_testcass.moduleid = t_modules.id\
    LEFT JOIN t_reports ON t_reports.cassid = t_testcass.id"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/getcassres",methods=["POST"])
def getcassres():
    '''
    获取用例执行结果
    {"pid":1}
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    sql = "select result from t_reports WHERE cassid = %s order by id DESC limit 1" % pid
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
        "moduleid":1,
        "testname":"测试用例名称",
        "testtype":"testcass",
        "explain":"用例描述",
        "request":{},
        "validate":[],
        "extract":[],
        "leader":"LangJin",
        "remark":"备注信息"
    }
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    moduleid = dictdata["moduleid"]
    testname = dictdata["testname"]
    testtype = dictdata["testtype"]
    explain = dictdata["explain"]
    requests = dict_to_dbjson(dictdata["request"])
    validate = dict_to_dbjson(dictdata["validate"])
    extract = dict_to_dbjson(dictdata["extract"])
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "UPDATE `t_testcass`\
        SET `moduleid` = '%s',\
        `testname` = '%s',\
        `testtype` = '%s',\
        `explain` = '%s',\
        `request` = '%s',\
        `validate` = '%s',\
        `extract` = '%s',\
        `leader` = '%s',\
        `remark` = '%s'\
        WHERE (`id` = '%s')" % (moduleid,testname,testtype,explain,requests,validate,extract,leader,remark,pid)
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "更新成功！！！"
    return jsonify(response)


@bp.route("/runtests", methods=["POST"])
def runtests():
    '''{"idlist":"1,2"}'''
    dictdata = request.get_json()
    idlist = dictdata["idlist"]
    sql = "select testname,testtype,request,validate,extract from t_testcass where id in(%s);" % idlist
    res = dbfucs.query(sql)
    jsoncasss = []
    for test in res:
        jsoncasss.append(test)
    # print(jsoncasss)
    for i in collect.collect_db_cass(jsoncasss):
        Logger.info("*" * 90)
    Logger.info("共计[%d]条测试用例执行完成！" % len(jsoncasss))
    Logger.info("*" * 90)
    response = {}
    response["code"] = 200
    response["msg"] = "成功！！！"
    return jsonify(response)
