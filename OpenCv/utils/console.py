# -*- coding:utf-8 -*-
from colorama import init, Fore, Back, Style
init()

class console(object):
    def __init__(self):
        pass

    @staticmethod
    def log(msg):
        print(Fore.BLACK + Back.WHITE+'[Log]'+msg)
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
        pass

    @staticmethod
    def warning(msg):
        print(Fore.BLACK + Back.YELLOW+'[Warning]'+msg)
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
        pass

    @staticmethod
    def error(msg):
        print(Fore.BLACK + Back.RED+'[Error]'+msg)
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
        pass
