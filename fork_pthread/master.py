# -*- coding:utf-8 -*-

import random,time,queue
from multiprocessing.managers import BaseManager


class QueueManger():
    pass

if __name__ == "__main__":
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    QueueManger.register('get_task_queue',callable=lambda :task_queue)
    QueueManger.register('get_result_queue',callable=lambda :result_queue)

    manger = QueueManger(address=('',5000),authkey=b'abc')
    manger.start()

    task = manger.get_task_queue()
    result = manger.get_result_queue()

    for i in range(5):
        n = random.randint(0,1000)
        print('Put task %d...' % (n))
        task.put(n)

    print('Try get results...')
    for i in range(5):
        r = result.get(timeout=10)
        print('Result:%s' % r)

    manger.shutdown()
    print('Master end...')
