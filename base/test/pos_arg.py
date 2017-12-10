#/usr/bin/python3
#-*- coding:utf-8 -*-

def power(x,n = 2):
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s


if (__name__ == "__main__"):
    print("hello")