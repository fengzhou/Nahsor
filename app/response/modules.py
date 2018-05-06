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


@bp.route("/getmodule",methods=["GET"])
def getmodule():
    '''
    读取项目列表，这个接口是给新增项目等东西的时候，选择所属项目用的
    '''
    sql = "SELECT * FROM t_module"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/addmodule",methods=["POST"])
def addmodule():
    '''
    新增项目
    {
        "moduleid":"所属产品id",
        "module":"项目名称",
        "explain":"描述",
        "leader":"责任人",
        "remark":"备注"
    }
    '''
    dictdata = request.get_json()
    moduleid = dictdata["moduleid"]
    module = dictdata["module"]
    explain = dictdata["explain"]
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "insert into t_module values(null,'%s','%s','%s','%s','%s',null,null);" % (moduleid,module,explain,leader,remark)
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "新增成功！！！"
    return jsonify(response)


@bp.route("/querymodule",methods=["GET"])
def querymodule():
    '''
    查询模块列表
    '''
    sql = "SELECT\
        t_modules.id as moduleid,\
        t_modules.modules,\
        t_modules.`explain`,\
        (SELECT COUNT(*) FROM t_testcass WHERE t_testcass.moduleid = t_modules.id) AS cassnum,\
        t_modules.leader,\
        t_modules.remark,\
        t_modules.createtime,\
        t_modules.updatatime\
    FROM\
        t_modules\
    LEFT JOIN t_testcass ON t_modules.id = t_testcass.moduleid\
    -- WHERE t_module.productid = 2\
    group by t_modules.id;"
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/deletemodule",methods=["POST"])
def deletemodule():
    '''
    删除项目
    {"pid":1}
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    sql = "DELETE FROM `t_module` WHERE (`id`='%s')" % pid
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "删除成功！！！"
    return jsonify(response)


@bp.route("/readmodule",methods=["POST"])
def readmodule():
    '''
    读取项目信息
    {"pid":1}
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    sql = "SELECT\
        t_module.moduleid,\
        t_module.module,\
        t_module.`explain`,\
        t_module.leader,\
        t_module.remark,\
        t_module.moduleid\
        FROM\
        t_module\
        WHERE\
        t_module.id = %s" % pid
    res = dbfucs.query(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "查询成功！！！"
    return jsonify(response)


@bp.route("/updatamodule",methods=["POST"])
def updatamodule():
    '''
    更新产品信息
    {
        "pid":2,
        "module":"产品名称",
        "explain":"描述",
        "leader":"责任人",
        "remark":"备注"
    }
    '''
    dictdata = request.get_json()
    pid = dictdata["pid"]
    moduleid = dictdata["moduleid"]
    module = dictdata["module"]
    explain = dictdata["explain"]
    leader = dictdata["leader"]
    remark = dictdata["remark"]
    sql = "UPDATE `t_module`\
        SET `moduleid` = '%s',\
        `module` = '%s',\
        `explain` = '%s',\
        `leader` = '%s',\
        `remark` = '%s'\
        WHERE (`id` = '%s')" % (moduleid,module, explain, leader, remark, pid)
    res = dbfucs.excute(sql)
    response = {}
    response["code"] = 200
    response["data"] = res
    response["msg"] = "更新成功！！！"
    return jsonify(response)


@bp.route("/runmodule",methods=["POST"])
def runmodule():
    '''
    按产品执行所有用例
    {"idlist":"1,2"}
    '''
    dictdata = request.get_json()
    idlist = dictdata["idlist"]
    sql = "SELECT * FROM t_testcass WHERE moduleid in (%s)" % idlist
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
