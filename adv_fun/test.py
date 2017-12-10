#!/usr/bin/python3
#-*-coding:utf-8-*-

'高级函数模块测试'

__author__ = 'akon'

import time

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#带参数的修饰器，text为修饰器
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#@log
@log1('执行')
def now():
    return time.ctime(time.time())

if __name__ == "__main__":
    print(now())
    pass
else:
    print("模块被import")