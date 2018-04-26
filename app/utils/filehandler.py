# -*- coding:utf-8 -*-
__author__ = "snake"


import os, codecs


def make_file(path):
    """
    :ex: 创建文件
    :param path: 文件路径
    :return: false 失败， true 成功
    """
    if not os.path.exists(path):
        try:
            with open(path, 'w', encoding='utf8') as file:
                file.close()
            return True
        except:
            return False
