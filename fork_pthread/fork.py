#!/usr/bin/python3
# -*- coding:utf-8 -*-
'进程测试'
__author__ = 'akon'

import os
from multiprocessing import Process

#fork只能用在Linux平台
def fun():
    print('Process (%s) start...' % (os.getpid()))

    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is (%s)' % (os.getpid(),os.getppid()))
    else:
        print('I am father process (%s) and my child is (%s)' % (os.getpid(),pid))


#windows
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
def fun1():
    print('Parent process %s.' % (os.getpid()))
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

if __name__ == "__main__":
    fun1()
    pass
