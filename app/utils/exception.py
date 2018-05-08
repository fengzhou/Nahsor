# -*- coding:utf-8 -*-

import json

try:
    FileNotFoundError = FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError

class MyBaseException(BaseException):
    pass

class FileFormatException(MyBaseException):
    pass

class ParamsException(MyBaseException):
    pass

class ResponseException(MyBaseException):
    pass

class ParseResponseException(MyBaseException):
    pass

class ValidationException(MyBaseException):
    pass

class NotFoundException(MyBaseException):
    pass

class FunctionNotFound(NotFoundException):
    pass

class VariableNotFound(NotFoundException):
    pass

class ApiNotFound(NotFoundException):
    pass

class SuiteNotFound(NotFoundException):
    pass

class TestcaseNotFound(NotFoundException):
    pass
