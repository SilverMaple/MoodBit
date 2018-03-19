# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 14:54
# @Author  : SilverMaple
# @Site    : https://github.com/SilverMaple
# @File    : decorators.py

from threading import Thread

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper