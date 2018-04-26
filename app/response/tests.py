# -*- conding:utf-8 -*-
__author__ = "SNake"
from flask import jsonify, request
from app import bp
from app.utils import dbfucs
from app.core import jsonfuc



@bp.route("/test")
def test():
    return jsonify({'code':200})