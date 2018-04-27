# -*- coding:utf-8 -*-
__author__="SNake"


import logging, datetime, os, ctypes, codecs
from functools import wraps


FOREGROUND_WHITE = 0x0007  # 白色文字
FOREGROUND_BLUE = 0x01  # 蓝色文字
FOREGROUND_GREEN = 0x02  # 绿色文字
FOREGROUND_RED = 0x04  # 红色文字
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN  # 文字黄色

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


def _exception_handle(func):
    """
    异常处理装饰器，确保代码不受日志影响
    :param func:
    :return: json
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass
    return wrapper

def _singleton(cls):
    """
    单例模式解决引用问题
    :param cls:
    :return:
    """
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


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


@_singleton
class Logger(object):
    def __init__(self, clevel=logging.INFO, Flevel=logging.DEBUG):
        # 创建日志文件
        path = os.getcwd()+"/app/logs/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"  # 默认为logs/yyyy-mm-dd.logs
        make_file(path)

        # 设置日志文件路径/格式/日志级别
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(fmt)
        self.sh.setLevel(clevel)

        # 设置文件日志
        self.fh = logging.FileHandler(path, encoding='utf-8')
        self.fh.setFormatter(fmt)
        self.fh.setLevel(Flevel)

        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)

    @_exception_handle
    def debug(self, message):
        """
        :ex: debug模式
        :param message: 输出消息
        :return:
        """
        self.logger.debug(message)
        self.close()

    @_exception_handle
    def info(self, message):
        """
        :ex: info模式
        :param message: 输出消息
        :return:
        """
        self.logger.info(message)
        self.close()

    @_exception_handle
    def war(self, message, color=FOREGROUND_YELLOW):
        """
        :ex: warrning模式
        :param message: 输出消息
        :return:
        """
        set_color(color)
        self.logger.warning(message)
        set_color(FOREGROUND_WHITE)
        self.close()

    @_exception_handle
    def error(self, message, color=FOREGROUND_RED):
        """
         :ex: error模式
         :param message: 输出消息， color: 输出颜色
         :return:
         """
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)
        self.close()

    @_exception_handle
    def cri(self, message, color=FOREGROUND_RED):
        """
         :ex: cri模式
         :param message: 输出消息， color: 输出颜色
         :return:
         """
        set_color(color)
        self.logger.critical(message)
        set_color(FOREGROUND_WHITE)
        self.close()

    @_exception_handle
    def close(self):
        self.sh.close()
        self.fh.close()


if __name__ == '__main__':
    logyyx = Logger(logging.WARNING, logging.DEBUG)
    logyyx.debug('debug信息')
    logyyx.info('info信息')
    logyyx.war('warning信息')
    logyyx.error('error信息')
    logyyx.cri('critical信息')

