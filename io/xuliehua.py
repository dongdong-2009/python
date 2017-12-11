#!/usr/bin/python3
# -*- coding:utf-8 -*-
'序列化测试'
__author__ = 'akon'

import pickle
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age  = age
        self.score = score

#普通序列化
def fun(op):
    d = dict(name='akon',age='20',score='100')
    #print(pickle.dumps(d))
    if op == 'w':
        with open('dump.txt','wb') as f:
            pickle.dump(d,f)
    elif op == 'r':
        with open('dump.txt', 'rb') as f:
            d = pickle.load(f)
            print(d)
    else:
        pass

#标准序列化json|xml|...
def fun1():
    d = dict(name='Bob', age=20, score=88)
    print(json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str))
    pass

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

#json与python对象转换
def fun2():
    s = Student('akon',20,100)
    #print(json.dumps(s,default = student2dict))
    print(json.dumps(s,default=lambda obj:obj.__dict__))
    pass

def fun3():
    json_str = '{"age":20,"score":90,"name":"akon"}'
    #json_str = '{"msg": {"args": "FE07000501010EFF", "dataType": "commonEvent"}, "server_id": "hos_server_01","device_id": "Y12E5B12E36D557AAC"}'
    print(json.loads(json_str,object_hook=dict2student).__dict__)

#格式化打印json
def fun4():
    data = {"msg": {"args": "FE07000501010EFF","dataType": "commonEvent"},"server_id": "hos_server_01","device_id": "Y12E5B12E36D557AAC"}
    print(json.dumps(data, sort_keys=True, indent=4))

if __name__ == "__main__":
    fun4()
    pass