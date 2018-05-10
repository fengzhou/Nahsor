# -*- coding:utf-8 -*-
import pymysql
import json
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'nahsor',
    'charset': 'utf8mb4'
}
db = pymysql.connect(**db_config)
cur = db.cursor()
d_json = {}
d_json = json.dumps(d_json)
tsql = "insert into jsondata(data) values('{json}')"
sql = tsql.format(json=pymysql.escape_string(d_json))
print(sql)
