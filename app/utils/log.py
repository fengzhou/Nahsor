# -*- coding:utf-8 -*-
import logging, datetime, os
import ctypes
from app.utils.filehandler import make_file

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    """内部函数
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


class Logger:
    def __init__(self, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        # 创建日志文件
        path = "../logs/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"  # 默认为logs/yyyy-mm-dd.log
        make_file(path)

        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        # 设置文件日志
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


    def debug(self, message):
        """
        :ex: debug模式
        :param message: 输出消息
        :return:
        """
        self.logger.debug(message)

    def info(self, message):
        """
        :ex: info模式
        :param message: 输出消息
        :return:
        """
        self.logger.info(message)

    def war(self, message, color=FOREGROUND_YELLOW):
        """
        :ex: warrning模式
        :param message: 输出消息， color: 输出颜色
        :return:
        """
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)

    def error(self, message, color=FOREGROUND_RED):
        """
         :ex: error模式
         :param message: 输出消息， color: 输出颜色
         :return:
         """
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger(logging.WARNING, logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')

