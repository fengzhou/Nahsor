# -*- coding:utf-8 -*-
__author__ = 'Jin'
'''
说明：操作数据库的相关方法封装
'''
import pymysql
from config import db_config


def query(sql=""):
    """
        ex: 根据sql查询结果
        args: sql
        return: results
    """
    results = []
    db = pymysql.connect(db_config)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        # 获得列名
        descs = []
        for desc in cur.description:
            descs.append(desc[0])
        # 构造键值对{"列名":数据}
        results = []
        for res in decode_result_date(cur.fetchall()):
            row = {}
            for i in range(len(descs)):
                row[descs[i]] = res[i]
            results.append(row)
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()  # 关闭连接
        return results
