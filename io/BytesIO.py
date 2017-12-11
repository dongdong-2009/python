#!/usr/bin/python3
# -*- coding:utf-8 -*-
'BytesIO test'
__author__ = 'akon'

from io import BytesIO

def fun():
    f = BytesIO()
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())
    pass

if __name__ == "__main__":
    fun()
    pass