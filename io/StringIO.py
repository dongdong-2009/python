
#!/usr/bin/python3
# -*- coding:utf-8 -*-
'StringIO test'
__author__ = "akon"

'''
    StringIO智能操作str
'''
from io import StringIO

def fun1(op):
    with StringIO() as f:
        if op == 'w':
            f.write("hello")
            print(f.getvalue())
        elif op == 'r':
            pass
        else:
            pass

def fun2():
    f = StringIO('akon\nloya\nfpyl')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())

if __name__ == "__main__":
    fun2()
    pass