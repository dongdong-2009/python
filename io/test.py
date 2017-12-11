#!/usr/bin/python3
# -*- coding:utf-8 -*-

def func1():
    try:
        f = open("D:\mkk_git\python\io\\file",'r')
        print(f.read())
    except IOError as e:
        print(e.strerror)
    finally:
        print("=======end=========")
        if f:
            f.close()

#读取一行
def func2(op):
    with open('D:\mkk_git\python\io\\file','a') as f:
        if op == 'r':
            for line in  f.readlines():
                print(line.strip())
        elif op == 'w':
            f.write("\nwrite file")
        else:
            pass

#读二进制图片
def func_picture():
    with open("D:\mkk_git\python\io\\1.jpg",'rb') as f:
        for line in f.readlines():
            print(line.strip())

if __name__ == "__main__":
    func2('w')
    pass