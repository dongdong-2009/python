#!/usr/bin/python3
# -*- coding:utf-8 -*-

'测试python面向对象'
__author__ = 'akon'

class Student(object):
    count = 0    #类属性，Student.count或者实例.count调用
    def __init__(self,name,score,age):
        self.name,self.score = name,score #公有变量
        self.__age = age #私有变量

    def print_score(self):
        print("%s:%s" % (self.name,self.score))

    def getAge(self):
        return self.__age

    def getLocals(self):
        print(locals())

    def __le__(self):
        return 100

if __name__ == "__main__":
    akon = Student('akon','80',10)
    Student.count = Student.count + 1
    loya = Student('loya','90',20)
    Student.count = Student.count + 1

    #print(akon.__age) #类的私有属性无法直接访问
    #akon.__state = "ok" 这是动态给实例添加的属性在类外部是可以访问的
    akon.print_score()
    #print(akon.__le__())
    #print("akon age:",akon.getAge())
    #akon.getLocals()
    loya.print_score()

    print("Total nums:",Student.count)
    pass
else:
    print("面向对象测试模块被调用")