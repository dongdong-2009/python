#!/usr/bin/python3
# -*- coding:utf-8 -*-
'进程池测试'
__author__ = 'akon'

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print("Run task %s (%s)..." % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name,(end-start)))
    #pass

def fun():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')
    #pass

if __name__ == "__main__":
    fun()
    pass