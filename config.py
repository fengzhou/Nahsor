# -*- coding:utf-8 -*-
'''
flask/db/other配置文件
'''
__author__ = 'Jin'

import os


# 开发环境
class DevelopmentConfig:
    # FLASK启动配置
    DEBUG = True
    HOST = "0.0.0.0"
    JSON_AS_ASCII = False #json 中文支持
    SECRET_KEY = os.urandom(24)    # SESSION配置


# 线上发布环境
class ProductionConfig:
    # FLASK启动配置
    DEBUG = True
    HOST = "0.0.0.0"
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = os.urandom(24)    # SESSION配置

config = {
    "DevelopmentConfig": DevelopmentConfig,
    "ProductionConfig": ProductionConfig
    }

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'nahsor',
    'charset': 'utf8mb4'
}
